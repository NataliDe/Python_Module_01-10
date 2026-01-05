def water_plants(plant_list):
    """Water plants and always close the watering system."""
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise Exception
            print(f"Watering {plant}")
    except Exception:
        print("Error: Cannot water None- invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Demonstrate finally block behavior."""
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
