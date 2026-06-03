import sys
import numpy as np
import scipy
import pandas as pd
import matplotlib

def main():
    print("Python version:", sys.version)
    print("NumPy version:", np.__version__)
    print("SciPy version:", scipy.__version__)
    print("Pandas version:", pd.__version__)
    print("Matplotlib version:", matplotlib.__version__)

    a = np.array([1, 2, 3])
    print("NumPy test:", a * 2)

    print("Environment test passed.")

if __name__ == "__main__":
    main()
