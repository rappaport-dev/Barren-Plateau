import os
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from tqdm import tqdm

from MILT_optimization import *

import sys
sys.path.append('../..') 

"""
Run this file to collect our data for the barren plateaus optimization runs.
"""

if __name__ == "__main__":
    print("Optimizations running!")

    # Set seeds for absolute reproducibility of measurement placements
    np.random.seed(42)
    random.seed(42)

    # Base directory for all outputs
    base_dir = "optimization_data"
    os.makedirs(base_dir, exist_ok=True)

    ansatz = "HEA2"
    n_qubits = 8
    n_layers = 16
    n_shots = 1 # change this line as needed
    post_selected = True # change this line as needed
    parallel = False
    gradient = "aware"
    ham_type = "z0z1"

    # Which probabilities you wish to loop through 
    probabilities = [0.80]

    # Manage thetas securely inside the data directory
    thetas_path = os.path.join(base_dir, "thetas.npy")
    if not os.path.exists(thetas_path):
        thetas = [random_parameters(num_parameters(n_qubits, n_layers, ansatz)) for _ in range(10)]
        print("Generated new thetas:", thetas)
        np.save(thetas_path, thetas)
    else:
        print(f"'{thetas_path}' already exists. Not overwriting.")
        thetas = np.load(thetas_path)

    # For this specific run, we are just using the first theta vector
    thetas = [thetas[0]]
    

    measurements_list = [random_measurements_prob(n_layers, n_qubits, p) for p in probabilities]
    print("Measurements generated.")

    for probability, measurements in tqdm(zip(probabilities, measurements_list), total=len(probabilities), desc="Probabilities"):
        
        # Route optimization run data into a specific subfolder
        dir_name = os.path.join(base_dir, f"new_prob_{probability}")

        results = multiple_optimization_runs(
            ansatz, n_qubits, n_layers, measurements, n_shots, post_selected, 
            dir_name, parallel, ham_type, gradient, thetas
        )

        for run_i, result in enumerate(results):
            parameters = result[0] # final optimized parameters

            N = 100
            n_param = len(parameters)
            scale = 0.1

            v1 = np.random.rand(n_param)
            v2 = np.random.rand(n_param)
            v1 = (v1 - 0.5) * scale
            v2 = (v2 - 0.5) * scale

            C = np.zeros((N, N))
            X = np.zeros((N, N))
            Y = np.zeros((N, N))

            for i in tqdm(range(N), desc="Landscape Grid X", leave=False):
                for j in tqdm(range(N), desc="Landscape Grid Y", leave=False):
                    x = parameters + (i - N / 2) * v1 + (j - N / 2) * v2
                    X[i, j] = (i - N / 2) / scale
                    Y[i, j] = (j - N / 2) / scale
                    
                    # Compute cost at grid point
                    grid_result = gradients_by_layer(
                        n_qubits, n_layers, x, gradient_technique="analytic", 
                        measurements=measurements, return_analytic_suite=True, 
                        post_selected=post_selected, periodic=True, 
                        get_layered_results=False, ham_type=ham_type, 
                        ansatz=ansatz, rotations=None
                    )
                    C[i, j] = grid_result[0] 

            # Plotting 
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, C, cmap=cm.coolwarm, linewidth=0, antialiased=False)
            
            # Save plot and data nicely inside the specific run directory
            plot_file = os.path.join(dir_name, f'landscape_{ham_type}_{probability}_{run_i}.pdf')
            data_file = os.path.join(dir_name, f'XYC_{ham_type}_{probability}_{run_i}.npy')
            
            plt.savefig(plot_file, transparent=True, dpi=500)
            plt.close(fig) # Prevent matplotlib from keeping the figure open in memory
            
            np.save(data_file, np.stack((X, Y, C), axis=0))