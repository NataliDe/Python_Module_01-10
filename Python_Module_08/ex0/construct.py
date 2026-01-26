#!/usr/bin/env python3
"""
Exercise 0: Entering the Matrix

This program checks whether it is running inside a Python virtual environment
and displays information about the current Python setup.
"""

import sys
import site


def is_virtual_env() -> bool:
    """
    Check if the program is running inside a virtual environment.

    If sys.prefix is different from sys.base_prefix,
    it means a virtual environment is active.
    """
    return sys.prefix != sys.base_prefix


def main() -> None:
    """Main program logic."""

    # Check virtual environment status
    if is_virtual_env():
        print("MATRIX STATUS: Welcome to the construct")
        print()
        # Show which Python executable is used
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: Active")
        print(f"Environment Path: {sys.prefix}")
        print()

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()

        # Show where packages are installed
        site_packages = site.getsitepackages()
        print("Package installation path:")
        for path in site_packages:
            print(path)

    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        # Instructions for creating and activating a venv
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
