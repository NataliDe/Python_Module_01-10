"""
Plant growth simulation.

This module demonstrates a simple Plant class and simulates
one week of growth and aging.
"""


class Plant:
    """Represent a plant that can grow and age over time."""

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name: Name of the plant.
            height_cm: Initial height in centimeters.
            age_days: Initial age in days.
        """
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm: int = 1) -> None:
        """
        Increase the plant height.

        Args:
            cm: Number of centimeters to grow.
        """
        self.height_cm += cm

    def age(self, days: int = 1) -> None:
        """
        Increase the plant age.

        Args:
            days: Number of days to age.
        """
        self.age_days += days

    def get_info(self) -> str:
        """
        Return current plant information.

        Returns:
            A formatted string with plant status.
        """
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


def main() -> None:
    """
    Run a one-week plant growth simulation.
    """
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)

    start_rose_height = rose.height_cm

    print("=== Day 1 ===")
    print(rose.get_info())

    for _ in range(7):
        rose.grow(1)
        rose.age(1)
        sunflower.grow(1)
        sunflower.age(1)

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height_cm - start_rose_height}cm")


if __name__ == "__main__":
    main()
