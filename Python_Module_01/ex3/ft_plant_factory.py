"""
Plant factory output.

This module creates several Plant objects and prints
their summaries along with the total count.
"""


class Plant:
    """Represent a plant with basic attributes."""

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
            A formatted string describing the plant.
        """
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"


def main() -> None:
    """
    Main function that creates plants and prints their information.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.summary()}")
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
