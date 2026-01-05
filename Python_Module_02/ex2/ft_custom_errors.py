class GardenError(Exception):
    """Base exception for all garden-related problems."""

    def __init__(self, message="A garden error occurred!"):
        super().__init__(message)


class PlantError(GardenError):
    """Exception for plant-specific problems."""

    def __init__(self, message="A plant error occurred!"):
        super().__init__(message)


class WaterError(GardenError):
    """Exception for watering-specific problems."""

    def __init__(self, message="A watering error occurred!"):
        super().__init__(message)


def raise_plant_error():
    """Raise a PlantError to demonstrate custom exceptions."""
    raise PlantError("The tomato plant is wilting!")


def raise_water_error():
    """Raise a WaterError to demonstrate custom exceptions."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """Demonstrate catching custom garden errors without crashing."""
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as exc:
        print(f"Caught PlantError: {exc}")

    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as exc:
        print(f"Caught WaterError: {exc}")

    print("Testing catching all garden errors...")
    for fn in (raise_plant_error, raise_water_error):
        try:
            fn()
        except GardenError as exc:
            print(f"Caught a garden error: {exc}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
