
def check_temperature(temp_str):
    """Validate temperature input for plant-friendly range (0 to 40)."""
    try:
        t = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if t > 40:
        print(f"Error: {t}°C is too hot for plants (max 40°C)")
        return None
    elif t < 0:
        print(f"{t}°C is too cold for plants (min 0°C)")
        return None
    print(f"Temperature {t}°C is perfect for plants!")
    return None


def test_temperature_input():
    """Run a small demo test suite to prove errors don't crash the program."""
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        print(f"\nTesting temperature: {value}")
        check_temperature(value)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
