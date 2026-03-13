import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0, "../..")


"""
This version of the code calculates and plots mutual info from samples. 
"""

if __name__ == "__main__":
    n_ap = 1000
    qubits = [4, 6, 8, 10, 12, 14, 16, 18]
    n_layers = 60
    probs = [0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]

    # results are in shape (num_qubits, num_prob,n_layers,2)
    results = np.load("data/aggregated_data_bootstrap.npy")

    for i, n_qubits in enumerate(qubits):
        results_for_each_p = []
        er_each_p = []

        examined_layer = 2 * n_qubits

        for j, p in enumerate(probs):
            mean = results[i, j, 0]
            low = results[i, j, 1]
            high = results[i, j, 2]

            # print("mean, low, high")
            # print(mean,low,high)
            # print("error bar sizes")

            # Load your data based on n_qubits and p
            results_for_each_p.append(mean)
            er_each_p.append((mean - low, high - mean))

        yerr = np.array(
            [[abs(err[0]) for err in er_each_p], [err[1] for err in er_each_p]]
        )

        # print("probs",probs)
        # print("results for each p", results_for_each_p)
        # print("yerr", er_each_p)
        plt.errorbar(
            x=probs, y=results_for_each_p, yerr=yerr, label=f"{n_qubits}", marker="."
        )

    plt.xlabel("Probability")
    plt.ylabel("Mutual information")
    plt.legend(title="number of qubits")
    plt.yscale("log")
    plt.title("Mutual info vs probability at 2n layers")
    plt.savefig("probability_at_layer_2n_bootstrap.png")
    plt.clf()
