def garden_operations():
    """Demonstrate common Python errors in a garden-themed program."""
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    plants = {"rose": 3, "tulip": 5}
    try:
        plants["missing_plant"]
    except KeyError as exc:
        print(f"Caught KeyError: {exc}\n")

    print("Testing multiple errors together...")
    try:
        int("not_a_number")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    """Run the demo and confirm the program does not crash."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
