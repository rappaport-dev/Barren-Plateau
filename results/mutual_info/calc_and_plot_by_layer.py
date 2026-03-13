import numpy as np
import matplotlib.pyplot as plt
import sys
import distinctipy

sys.path.insert(0, "../..")
from MILT_mutual_information import mutual_info_standard_error

"""
This script calculates and plots mutual information across circuit layers 
for various system sizes (qubits). This generates the core mutual information
scaling figures for the manuscript.
"""

if __name__ == "__main__":
    qubits = [4, 6, 8, 10, 12, 14, 16]
    n_layers = 60

    # Currently configured to plot the baseline case (p=0)
    probs = [0]

    # Generate distinct, colorblind-friendly colors for each system size
    num_colors = len(qubits)
    colors = distinctipy.get_colors(num_colors)

    # Create subplots: one row for each probability
    fig, axs = plt.subplots(len(probs), 1, figsize=(10, len(probs) * 5))
    if len(probs) == 1:
        axs = [axs]

    for j, p in enumerate(probs):
        for i, n_qubits in enumerate(qubits):
            # Handles the legacy file naming conventions from the data collection phase
            if p == 0:
                # Load pre-aggregated results for the no-measurement baseline
                mean, error = np.load(f"data/{n_qubits}_{p}_layeredresults.npy")

            elif n_qubits in [12, 14]:
                # Load specific 1000-sample batches
                p_i_m_given_thetas = np.load(
                    f"data/{n_qubits}_{p}_layeredresults_samples_changeboth_1000.npy"
                )
                mean, error = mutual_info_standard_error(p_i_m_given_thetas)

            else:
                # Load default raw sample batches
                p_i_m_given_thetas = np.load(
                    f"data/{n_qubits}_{p}_layeredresults_samples_changeboth.npy"
                )
                mean, error = mutual_info_standard_error(p_i_m_given_thetas)

            # Filter out any layers where the error calculation resulted in NaN
            valid_mask = ~np.isnan(error)
            clean_mean = mean[valid_mask]
            clean_error = error[valid_mask]
            x_layers = np.arange(n_layers)[valid_mask]

            # --- PLOTTING ---
            axs[j].errorbar(
                x=x_layers,
                y=clean_mean,
                yerr=clean_error,
                label=f"{n_qubits} qubits",
                color=colors[i],
                marker="x",
            )

        # --- FORMATTING ---
        axs[j].set_yscale("log")

        # Set the y-axis to show exact powers of 2 for clean visualization
        yticks = [2.0 ** (-i) for i in range(17)]
        yticklabels = [f"{ytick:g}" for ytick in yticks]
        axs[j].set_yticks(yticks)
        axs[j].set_yticklabels(yticklabels)

        axs[j].set_xlabel("Layers")
        axs[j].set_ylabel("Mutual information")
        axs[j].set_title(f"Mutual Information vs. Layers (p = {p})")
        axs[j].legend(fontsize=12, title="Number of qubits")

    plt.tight_layout()
    plt.savefig(f"mutual_info_by_layer_p{probs[0]}.pdf", bbox_inches="tight")
    plt.show()
