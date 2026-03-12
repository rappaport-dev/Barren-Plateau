"""
Run this file to collect our data for the barren plateaus optimization runs. 
"""

import sys
sys.path.append('../..') 

from MILT_gradient_results import *

if __name__ == "__main__":

    qubit_range = [10]  # 
    n_layers = 60
    n_samples = 5000
    probability_range = [i * .05 for i in range(20)]
    ansatz = "HEA2"
    # ham_type = "z0z1"
    ham_type = "xxz_1_1_05"
    file_name = "tenqubits"

    # this saves some files to your harddrive
    # note this is set to generate 67% confidence intervals
    generate_results(qubit_range, n_layers, n_samples,
                     probability_range, ansatz, file_name, ham_type, parallel=True)
