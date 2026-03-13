"""
Run this file to collect our data for the barren plateaus optimization runs.

Currently set to a tiny system size.
"""

import sys

sys.path.append("../..")

from MILT_gradient_results import *

if __name__ == "__main__":
    qubit_range = [2]  #
    n_layers = 10
    n_samples = 50
    probability_range = [i * 0.05 for i in range(20)]
    ansatz = "HEA2"
    # ham_type = "z0z1"
    ham_type = "xxz_1_1_05"
    file_name = "tenqubits"

    # this saves some files to your harddrive
    # note this is set to generate 67% confidence intervals
    generate_results(
        qubit_range,
        n_layers,
        n_samples,
        probability_range,
        ansatz,
        file_name,
        ham_type,
        parallel=False,
    )
