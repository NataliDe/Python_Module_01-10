#!/usr/bin/env python3
"""
Exercise 01: Loading Programs

- Checks dependencies (pandas, numpy, matplotlib, requests)
- Prints installed versions (if available)
- If everything is installed: simulates "Matrix data" and saves a plot
"""

import sys
import importlib


REQUIRED = ["pandas", "numpy", "matplotlib"]
OPTIONAL = ["requests"]
OUTPUT_FILE = "matrix_analysis.png"


def module_available(module_name: str) -> bool:
    """Return True if module can be imported."""
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def module_version(dist_name: str):
    """
    Return installed version of a distribution, or None if unavailable.

    Uses importlib.metadata (built-in in Python 3.10+).
    """
    try:
        from importlib.metadata import version
        return version(dist_name)
    except Exception:
        return None


def print_dependency_status() -> bool:
    """
    Print dependency check results.
    Return True if all required deps are available.
    """
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    all_ok = True

    for name in REQUIRED:
        if module_available(name):
            ver = module_version(name)
            ver_str = ver if ver is not None else "unknown"
            print(f"[OK] {name} ({ver_str}) - Ready")
        else:
            all_ok = False
            print(f"[MISSING] {name} - Not installed")

    for name in OPTIONAL:
        if module_available(name):
            ver = module_version(name)
            ver_str = ver if ver is not None else "unknown"
            print(f"[OK] {name} ({ver_str}) - Optional ready")
        else:
            print(f"[SKIP] {name} - Optional not installed")

    return all_ok


def print_install_instructions() -> None:
    """Print pip and Poetry installation hints."""
    print()
    print("Some required dependencies are missing.")
    print("Install with pip:")
    print("  pip install -r ex01/requirements.txt")
    print()
    print("Or install with Poetry:")
    print("  poetry install")
    print("  poetry run python ex01/loading.py")


def run_analysis() -> None:
    """Simulate data analysis and save a simple visualization."""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")

    n_points = 1000
    print(f"Processing {n_points} data points...")

    rng = np.random.default_rng(42)
    signal = rng.normal(loc=0.0, scale=1.0, size=n_points).cumsum()

    df = pd.DataFrame({"tick": range(n_points), "signal": signal})
    df["moving_avg"] = df["signal"].rolling(window=30, min_periods=1).mean()

    print("Generating visualization...")

    plt.figure()
    plt.plot(df["tick"], df["signal"], label="signal")
    plt.plot(df["tick"], df["moving_avg"], label="moving_avg")
    plt.legend()
    plt.title("Matrix Signal Analysis")
    plt.xlabel("tick")
    plt.ylabel("value")
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE)

    print("Analysis complete!")
    print(f"Results saved to: {OUTPUT_FILE}")


def main() -> None:
    """Entry point."""
    ok = print_dependency_status()

    print()
    print(f"Current Python: {sys.executable}")
    print(f"Env prefix: {sys.prefix}")
    print(f"Base prefix: {getattr(sys, 'base_prefix', sys.prefix)}")
    print()

    if not ok:
        print_install_instructions()
        return

    run_analysis()


if __name__ == "__main__":
    main()
