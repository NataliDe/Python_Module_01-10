#!/usr/bin/env python3

"""
Simple garden program.

Demonstrates program entry point and formatted output.
"""


def main() -> None:
    """
    Main function that prints basic plant information.
    """
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
