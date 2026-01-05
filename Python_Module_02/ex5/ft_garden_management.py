class GardenError(Exception):
    """Base exception for garden-related problems."""


class PlantError(GardenError):
    """Raised when a plant-related problem occurs."""


class WaterError(GardenError):
    """Raised when a watering-related problem occurs."""


class GardenManager:
    """Simple garden manager demonstrating error handling techniques."""

    def __init__(self):
        self.plants = {}

    def add_plant(self, plant_name):
        """Add a plant to the garden (plant name must be non-empty)."""
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if plant_name not in self.plants:
            self.plants[plant_name] = {"water": 5, "sun": 8}

    def set_plant_conditions(self, plant_name, water_level, sun_hours):
        """Set plant conditions for health checks."""
        if plant_name not in self.plants:
            raise PlantError("Plant does not exist!")
        self.plants[plant_name]["water"] = water_level
        self.plants[plant_name]["sun"] = sun_hours

    def water_plants(self):
        """Water all plants and always close the watering system."""
        print("Opening watering system")
        try:
            for name in self.plants:
                print(f"Watering {name}- success")
        except Exception:
            print("Error: watering system failure!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name):
        """Check plant health and raise errors for invalid conditions."""
        if plant_name not in self.plants:
            raise PlantError("Plant does not exist!")

        water_level = self.plants[plant_name]["water"]
        sun_hours = self.plants[plant_name]["sun"]

        if water_level < 1:
            raise PlantError(
                f"Water level {water_level} is too low (min 1)"
            )
        if water_level > 10:
            raise PlantError(
                f"Water level {water_level} is too high (max 10)"
            )

        if sun_hours < 2:
            raise PlantError(
                f"Sunlight hours {sun_hours} is too low (min 2)"
            )
        if sun_hours > 12:
            raise PlantError(
                f"Sunlight hours {sun_hours} is too high (max 12)"
            )

        return (
            f"{plant_name}: healthy "
            f"(water: {water_level}, sun: {sun_hours})"
        )


def main():
    """Run a demo of the garden management system."""
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        print("Added tomato successfully")
    except PlantError as exc:
        print(f"Error adding plant: {exc}")

    try:
        manager.add_plant("lettuce")
        print("Added lettuce successfully")
    except PlantError as exc:
        print(f"Error adding plant: {exc}")

    try:
        manager.add_plant("")
        print("Added  successfully")
    except PlantError as exc:
        print(f"Error adding plant: {exc}")

    print("Watering plants...")
    manager.water_plants()

    manager.set_plant_conditions("tomato", 5, 8)
    manager.set_plant_conditions("lettuce", 15, 8)

    print("Checking plant health...")
    try:
        print(manager.check_plant_health("tomato"))
    except PlantError as exc:
        print(f"Error checking tomato: {exc}")

    try:
        print(manager.check_plant_health("lettuce"))
    except PlantError as exc:
        print(f"Error checking lettuce: {exc}")

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as exc:
        print(f"Caught GardenError: {exc}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
