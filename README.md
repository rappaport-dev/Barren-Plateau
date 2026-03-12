# Measurement Induced Landscape Transitions (MILT)

## Overview
This repository contains the source code for "Measurement-induced landscape transitions in hybrid variational quantum circuits," The code is structured to facilitate the reproduction of results and figures presented in the paper. Key computations are performed by four primary Python scripts, labeled `MILT_`, which are utilized by various other scripts stored along with their outputs in the `results` folder.

**Technical Summary**: the code is a high-performance Python library for analyzing **Measurement-Induced Landscape Transitions** in Variational Quantum Eigensolvers (VQE). This codebase implements parallelized gradient descent strategies to mitigate Barren Plateaus in hybrid quantum circuits.

### Features
* **Parallel Computing:** Utilizes **Dask** for lazy evaluation and parallel execution of quantum circuit simulations across multiple cores.
* **Optimization:** Implements custom gradient descent schedules with analytical gradient calculation.
* **Scalability:** Designed to handle parameter sweeps for high-dimensional ansatzes (HEA, HVA).

### Tech Stack
* **Python** (NumPy, SciPy)
* **Dask** (Parallel Task Scheduling)
* **OpenFermion** (Hamiltonian definitions)

## Installation
```bash
git clone https://github.com/rappaport-dev/Barren-Plateau.git
pip install -r requirements.txt
```

## **Running the Scripts**: 
Execute the script files as needed to regenerate the data for plots or to utilize the functions in the core files for further analysis or expansion.

## Core Files

The four core Python files (`MILT_` series) encompass the following functionalities:
1. `MILT_mutual_information.py`: Handles mutual information calculations.
2. `MILT_core.py`: Provides fundamental utilities and functions.
3. `MILT_gradient_results.py`: Focuses on gradient analysis in quantum circuits.
4. `MILT_optimization.py`: Implements the VQE algorithm and collects performance data.

## Results

The `results` folder includes scripts used for generating the data and their respective outputs. 
## Authors

- **Sonny Rappaport**: Primary developer and researcher.
- **Gaurav Gyawali**: Primary developer and researcher.
- **Michael Lawler**: Provided initial code structure and researcher.

## Citation

If you use this code in your research, please cite the accompanying paper.
