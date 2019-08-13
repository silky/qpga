import argparse
import sys

from tensorflow.python.keras import backend as K

sys.path.append("..")
from qpga import *

K.set_floatx('float64')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Run a fidelity search on QPGA with specified number of qubits")
    parser.add_argument('num_qubits', type = int)
    parser.add_argument('--start', type = int)

    args = parser.parse_args()
    N = args.num_qubits

    sys.stdout = Logger(f"NOON_fidelities_{N}_qubits.log")

    print(f"Running NOON-state fidelity search for {N} qubits...")

    if args.start:
        depths = list(range(args.start, 999))
    else:
        depths = list(range(N, 999))

    num_states = 1
    in_data = np.array([zero_state(N)] * num_states)
    out_data = np.array([noon_state(N)] * num_states)

    fidelities = fidelity_depth_search(depths,
                                       in_data = in_data,
                                       out_data = out_data,
                                       validation_split = 0.0,
                                       return_on_first_convergence = True)
