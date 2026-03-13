import os
import numpy as np
import sys

sys.path.insert(0, "../..")
from MILT_mutual_information import *

# This file is meant to work with our data, which has been saved in a few different formats as the code was developed.
# If generating new data, the process to plot the data is much easier and you won't need to work with different shapes.
# It calculates the confidence intervals from the raw data and saves it.


def load_and_aggregate_data(directory):
    # Parameters
    num_qubits_values = list(range(4, 20, 2))
    p_values = [0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
    n_layers = 60
    nap_values = [10000, 1000]  # Order matters: prefer 10000 samples over 1000

    # Initialize the aggregated data array
    # Shape: (qubits, probabilities, 3) where the 3 holds [mean, CI_low, CI_high]
    aggregated_data = np.full((len(num_qubits_values), len(p_values), 3), np.nan)

    # Iterate over all combinations of num_qubits, and probabilities
    for i, num_qubits in enumerate(num_qubits_values):
        for j, p_value in enumerate(p_values):
            file_found = False

            # Check for files with the preferred number of samples first
            for nap in nap_values:
                if file_found:
                    break
                # Skip p=0 for system sizes under 18 based on available data
                if p_value == 0 and num_qubits < 18:
                    continue
                else:
                    filename = f"{num_qubits}_{p_value}_{n_layers}layers_nap_{nap}.npy"

                    path = os.path.join(directory, filename)
                    if os.path.isfile(path):
                        file_data = np.load(path)
                        print(f"Loaded {filename} with shape {file_data.shape}")
                        file_found = True
                        mean, confidence_interval = mutual_info_bootstrap(
                            file_data, 2 * num_qubits
                        )

                        # Calculate mean and error across the axis corresponding to different samples (assuming axis 0)
                        # Store the results in the array
                        aggregated_data[i, j, 0] = mean  # Storing mean
                        aggregated_data[i, j, 1] = (
                            confidence_interval.low
                        )  # Storing error
                        aggregated_data[i, j, 2] = confidence_interval.high
                    else:
                        continue

    output_file = os.path.join(directory, "aggregated_data_bootstrap.npy")
    np.save(output_file, aggregated_data)
    print(f"Data aggregation complete and saved to {output_file}.")


if __name__ == "__main__":
    directory = "."
    load_and_aggregate_data(directory)
