"""
Garden plant types demonstration.

This module demonstrates inheritance using Plant as a base class
and Flower, Tree, and Vegetable as specialized subclasses.
"""


class Plant:
    """Base class representing a generic plant."""

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

    def base_info(self) -> str:
        """
        Return basic plant information.

        Returns:
            A formatted string with base plant data.
        """
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days"


class Flower(Plant):
    """Represent a flowering plant."""

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        color: str,
    ) -> None:
        """
        Initialize a Flower instance.

        Args:
            name: Name of the flower.
            height_cm: Height in centimeters.
            age_days: Age in days.
            color: Flower color.
        """
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self) -> None:
        """Print a blooming message."""
        print(f"{self.name} is blooming beautifully!")

    def info(self) -> str:
        """
        Return detailed flower information.

        Returns:
            A formatted string with flower details.
        """
        return f"{self.base_info()}, {self.color} color"


class Tree(Plant):
    """Represent a tree."""

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        trunk_diameter: int,
    ) -> None:
        """
        Initialize a Tree instance.

        Args:
            name: Name of the tree.
            height_cm: Height in centimeters.
            age_days: Age in days.
            trunk_diameter: Diameter of the trunk in centimeters.
        """
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        """
        Calculate the shade produced by the tree.

        Returns:
            Estimated shade area.
        """
        return (self.trunk_diameter * self.trunk_diameter) // 32

    def info(self) -> str:
        """
        Return detailed tree information.

        Returns:
            A formatted string with tree details.
        """
        return f"{self.base_info()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Represent a vegetable plant."""

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name: Name of the vegetable.
            height_cm: Height in centimeters.
            age_days: Age in days.
            harvest_season: Harvest season.
            nutritional_value: Nutritional value description.
        """
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self) -> str:
        """
        Return detailed vegetable information.

        Returns:
            A formatted string with vegetable details.
        """
        return f"{self.base_info()}, {self.harvest_season} harvest"


def main() -> None:
    """
    Main function demonstrating different plant types.
    """
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    ]
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1500, 35),
    ]
    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 60, "autumn", "beta-carotene"),
    ]

    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.info()}")
        flower.bloom()

    for tree in trees:
        shade = tree.produce_shade()
        print(f"{tree.name} (Tree): {tree.info()}")
        print(f"{tree.name} provides {shade} square meters of shade")

    for vegetable in vegetables:
        print(f"{vegetable.name} (Vegetable): {vegetable.info()}")
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")


if __name__ == "__main__":
    main()
