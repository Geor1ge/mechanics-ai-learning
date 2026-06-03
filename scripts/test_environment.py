"""
Stage 0 environment test.

This script checks whether the basic scientific Python environment works.
"""

import sys
from pathlib import Path

import numpy as np
import scipy
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def main() -> None:
    print("=" * 60)
    print("Mechanics AI Learning - Environment Test")
    print("=" * 60)

    print(f"Python:     {sys.version.split()[0]}")
    print(f"NumPy:      {np.__version__}")
    print(f"SciPy:      {scipy.__version__}")
    print(f"Pandas:     {pd.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")

    # NumPy test
    x = np.linspace(0.0, 1.0, 101)
    y = np.sin(2.0 * np.pi * x)

    print("\nNumPy test:")
    print(f"x shape: {x.shape}")
    print(f"y max:   {y.max():.6f}")
    print(f"y min:   {y.min():.6f}")

    # Pandas test
    df = pd.DataFrame({"x": x, "y": y})
    print("\nPandas test:")
    print(df.head())

    # Matplotlib test
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("sin(2πx)")
    ax.set_title("Environment Test Plot")
    ax.grid(True)

    output_path = results_dir / "environment_test_plot.png"
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"\nPlot saved to: {output_path}")
    print("\nEnvironment test passed.")


if __name__ == "__main__":
    main()
