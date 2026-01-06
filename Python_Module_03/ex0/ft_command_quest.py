#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    total_args = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
        return

    args = sys.argv[1:]
    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(args)}")

    for i, arg in enumerate(args, 1):
        print(f"Argument {i}: {arg}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
