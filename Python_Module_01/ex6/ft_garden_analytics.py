"""
ft_garden_analytics.py

Garden management analytics demo.
"""


class Plant:
    """Base plant type."""

    def __init__(self, name: str, height_cm: int,
                 age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm: int = 1) -> None:
        self.height_cm += cm
        print(f"{self.name} grew {cm}cm")

    def info(self) -> str:
        return f"{self.name}: {self.height_cm}cm"


class FloweringPlant(Plant):
    """Plant that can bloom."""

    def __init__(self, name: str, height_cm: int,
                 age_days: int, color: str) -> None:
        super().__init__(name, height_cm, age_days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def info(self) -> str:
        suffix = ""
        if self.is_blooming:
            suffix = " (blooming)"
        return (
            f"{self.name}: {self.height_cm}cm, "
            f"{self.color} flowers{suffix}"
        )


class PrizeFlower(FloweringPlant):
    """Flower with prize points."""

    def __init__(self, name: str, height_cm: int,
                 age_days: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height_cm, age_days, color)
        self.prize_points = prize_points

    def info(self) -> str:
        suffix = ""
        if self.is_blooming:
            suffix = " (blooming)"
        return (
            f"{self.name}: {self.height_cm}cm, "
            f"{self.color} flowers{suffix}, "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    """Manage multiple gardens."""

    class GardenStats:
        """Statistics helpers."""

        @staticmethod
        def total_growth(before: list[int],
                         after: list[int]) -> int:
            return sum(a - b for b, a in zip(before, after))

        @staticmethod
        def validate_height(height_cm: int) -> bool:
            return height_cm >= 0

    total_gardens_managed = 0

    def __init__(self) -> None:
        self.gardens: dict[str, list[Plant]] = {}
        self._last_growth: dict[str, int] = {}

    def add_garden(self, owner: str) -> None:
        if owner not in self.gardens:
            self.gardens[owner] = []
            self._last_growth[owner] = 0
            GardenManager.total_gardens_managed += 1

    def add_plant(self, owner: str,
                  plant: Plant) -> None:
        self.add_garden(owner)
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def help_all_grow(self, owner: str,
                      cm: int = 1) -> None:
        plants = self.gardens.get(owner, [])
        before = [p.height_cm for p in plants]

        print(f"\n{owner} is helping all plants grow...")
        for plant in plants:
            plant.grow(cm)

        after = [p.height_cm for p in plants]
        self._last_growth[owner] = (
            GardenManager.GardenStats.total_growth(
                before, after
            )
        )

    def garden_report(self, owner: str) -> None:
        plants = self.gardens.get(owner, [])
        growth = self._last_growth.get(owner, 0)

        regular = sum(1 for p in plants
                      if type(p) is Plant)
        flowering = sum(
            1 for p in plants
            if isinstance(p, FloweringPlant)
            and not isinstance(p, PrizeFlower)
        )
        prize = sum(1 for p in plants
                    if isinstance(p, PrizeFlower))

        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in plants:
            print(f"- {plant.info()}")

        print(
            f"\nPlants added: {len(plants)}, "
            f"Total growth: {growth}cm"
        )
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, "
            f"{prize} prize flowers\n"
        )

    @classmethod
    def create_garden_network(cls) -> str:
        return f"Total gardens managed: {cls.total_gardens_managed}"

    @staticmethod
    def score_garden(plants: list[Plant]) -> int:
        score = 0
        for plant in plants:
            score += plant.height_cm
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points * 4
        return score


def main() -> None:
    print("\n=== Garden Management System Demo ===\n")

    manager = GardenManager()

    oak = Plant("Oak Tree", 100, 1000)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sun = PrizeFlower("Sunflower", 50, 45,
                      "yellow", 10)

    rose.bloom()
    sun.bloom()

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sun)

    manager.help_all_grow("Alice", 1)
    manager.garden_report("Alice")

    print(
        "Height validation test: "
        f"{GardenManager.GardenStats.validate_height(0)}"
    )

    alice_score = GardenManager.score_garden(
        manager.gardens["Alice"]
    )

    manager.add_garden("Bob")
    manager.gardens["Bob"].append(
        Plant("Mint", 92, 40)
    )
    bob_score = GardenManager.score_garden(
        manager.gardens["Bob"]
    )

    print(
        f"Garden scores- Alice: {alice_score}, "
        f"Bob: {bob_score}"
    )
    print(manager.create_garden_network())


if __name__ == "__main__":
    main()
