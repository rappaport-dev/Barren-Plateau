import sys
sys.path.append('../..') 

from MILT_gradient_results import * 

if __name__ == "__main__":

    results = np.load("data/HVAData517.npy")

    # loop over the qubits, i.e, third index of the array shape
    for i in range(np.shape(results)[2]):

        unaware_variance = results[0,:,i,0,0,-1]
        aware_variance = results[0,:,i,0,1,-1]
        unaware_error = results[0,:,i,1,:,-1].T
        aware_error = results[0,:,i,2,:,-1].T    

        plt.errorbar([(.05)*i for i in range(20)], aware_variance, yerr = (aware_variance-aware_error[0],aware_error[1]-aware_variance), marker='o',label=6+2*i)



    plt.yscale('log')
    plt.title("aware variance, HVA2, 100 layers, XXZ hamiltonian")
    plt.xlabel("Probability to Place Gate")
    plt.ylabel("aware Variance")
    plt.legend(title="qubits")
    plt.show()
