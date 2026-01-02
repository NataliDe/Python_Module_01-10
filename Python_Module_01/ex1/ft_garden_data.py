"""
Garden Plant Registry.

This module demonstrates a simple Plant class and prints
a registry of plants when run as a script.
"""


class Plant:
    """Represent a plant with basic characteristics."""

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name: Name of the plant.
            height_cm: Height of the plant in centimeters.
            age_days: Age of the plant in days.
        """
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def summary(self) -> str:
        """
        Return a short summary of the plant.

        Returns:
            A formatted string with plant details.
        """
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


def main() -> None:
    """
    Main function that creates plants and prints the registry.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant.summary())


if __name__ == "__main__":
    main()
