"""
Exercise 6: Garden Analytics Platform
File: ft_garden_analytics.py

Goal: fully reproduce the example output from the subject.
Authorized: class, __init__, super(), print(), staticmethod(), classmethod()
"""


class Plant:
    """Base plant."""

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm: int = 1) -> None:
        """Grow and print exactly like in the example."""
        self.height_cm += cm
        print(f"{self.name} grew {cm}cm")

    def info(self) -> str:
        """Info line for report."""
        return f"{self.name}: {self.height_cm}cm"


class FloweringPlant(Plant):
    """Plant that can bloom (has color)."""

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Make it bloom."""
        self.is_blooming = True

    def info(self) -> str:
        """Info line for report (exact style)."""
        state = "blooming" if self.is_blooming else "not blooming"
        return (
            f"{self.name}: {self.height_cm}cm, {self.color} flowers "
            f"({state})"
        )


class PrizeFlower(FloweringPlant):
    """Flower with prize points."""

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height_cm, age_days, color)
        self.prize_points = prize_points

    def info(self) -> str:
        """Info line for report (exact style)."""
        base = super().info()
        return f"{base}, Prize points: {self.prize_points}"


class GardenManager:
    """Manages multiple gardens and analytics."""

    class GardenStats:
        """Nested helper for statistics."""

        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth_cm = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0

        def register_plant(self, plant: Plant) -> None:
            """Update counters when a plant is added."""
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering += 1
            else:
                self.regular += 1

        def register_growth(self, cm: int) -> None:
            """Track growth."""
            self.total_growth_cm += cm

    class Garden:
        """Single garden with plants + stats."""

        def __init__(self, owner: str) -> None:
            self.owner = owner
            self.plants: list[Plant] = []
            self.stats = GardenManager.GardenStats()

        def add_plant(self, plant: Plant) -> None:
            """Add plant and update stats."""
            self.plants.append(plant)
            self.stats.register_plant(plant)

        def help_all_grow(self, cm: int = 1) -> None:
            """Grow every plant and print exactly like the example."""
            print(f"{self.owner} is helping all plants grow...")
            for plant in self.plants:
                plant.grow(cm)
                self.stats.register_growth(cm)

        def report(self) -> None:
            """Print report exactly like the example."""
            print(f"=== {self.owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.plants:
                print(f"- {plant.info()}")
            print(
                f"Plants added: {self.stats.plants_added}, "
                f"Total growth: {self.stats.total_growth_cm}cm"
            )
            print(
                "Plant types: "
                f"{self.stats.regular} regular, "
                f"{self.stats.flowering} flowering, "
                f"{self.stats.prize} prize flowers"
            )

        def score(self) -> int:
            """
            Score to match the example numbers.

            Rule used here:
            - sum of all plant heights
            - + prize points for PrizeFlower
            - + 15 points for EACH blooming FloweringPlant
            """
            total = 0
            for plant in self.plants:
                total += plant.height_cm
                if isinstance(plant, PrizeFlower):
                    total += plant.prize_points
                if isinstance(plant, FloweringPlant) and plant.is_blooming:
                    total += 15
            return total

    def __init__(self) -> None:
        self.gardens: dict[str, GardenManager.Garden] = {}

    def add_garden(self, owner: str) -> None:
        """Create garden if missing."""
        if owner not in self.gardens:
            self.gardens[owner] = GardenManager.Garden(owner)

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        """Add plant and print exactly like the example."""
        self.add_garden(owner)
        self.gardens[owner].add_plant(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def get_garden(self, owner: str) -> "GardenManager.Garden":
        """Get garden by owner."""
        return self.gardens[owner]

    def total_gardens(self) -> int:
        """How many gardens are managed."""
        return len(self.gardens)

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Class-level factory (works on the manager type itself)."""
        return cls()

    @staticmethod
    def is_valid_height(height_cm: int) -> bool:
        """Utility validation."""
        return height_cm >= 0


def main() -> None:
    """Run the exact demo shown in the subject."""
    manager = GardenManager.create_garden_network()

    manager.add_garden("Alice")
    manager.add_garden("Bob")

    oak = Plant("Oak Tree", 100, 3650)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    manager.add_plant_to_garden("Alice", oak)
    manager.add_plant_to_garden("Alice", rose)
    manager.add_plant_to_garden("Alice", sunflower)

    rose.bloom()
    sunflower.bloom()

    manager.get_garden("Alice").help_all_grow(1)
    manager.get_garden("Alice").report()

    print(f"Height validation test: {manager.is_valid_height(10)}")

    bob_garden = manager.get_garden("Bob")
    bob_garden.add_plant(Plant("Bob Plant", 92, 10))

    alice_score = manager.get_garden("Alice").score()
    bob_score = manager.get_garden("Bob").score()

    print("Garden scores")
    print(f"- Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {manager.total_gardens()}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    main()
