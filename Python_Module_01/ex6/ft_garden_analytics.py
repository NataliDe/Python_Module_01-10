class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm: int = 1) -> None:
        self.height_cm += cm
        print(f"{self.name} grew {cm}cm")

    def info(self) -> str:
        return f"{self.name}: {self.height_cm}cm"


class FloweringPlant(Plant):
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
        self.is_blooming = True

    def info(self) -> str:
        suffix = " (blooming)" if self.is_blooming else ""
        return (
            f"{self.name}: {self.height_cm}cm, {self.color} flowers{suffix}"
        )


class PrizeFlower(FloweringPlant):
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
        suffix = " (blooming)" if self.is_blooming else ""
        return (
            f"{self.name}: {self.height_cm}cm, {self.color} flowers{suffix}, "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    class GardenStats:
        @staticmethod
        def total_growth(before: list[int], after: list[int]) -> int:
            return sum(a - b for b, a in zip(before, after))

        @staticmethod
        def validate_height(height_cm: int) -> bool:
            return height_cm >= 0

    total_gardens_managed = 0

    def __init__(self) -> None:
        self.gardens: dict[str, list[Plant]] = {}

    def add_garden(self, owner: str) -> None:
        if owner not in self.gardens:
            self.gardens[owner] = []
            GardenManager.total_gardens_managed += 1

    def add_plant(self, owner: str, plant: Plant) -> None:
        self.add_garden(owner)
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def help_all_grow(self, owner: str, cm: int = 1) -> None:
        print(f"{owner} is helping all plants grow...")
        for p in self.gardens.get(owner, []):
            p.grow(cm)

    def garden_report(self, owner: str) -> None:
        plants = self.gardens.get(owner, [])
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")

        for p in plants:
            line = p.info()
            if isinstance(p, Plant) and not isinstance(p, FloweringPlant):
                print(f"- {line}")
            else:
                print(f"- {line}")

        heights = [p.height_cm for p in plants]
        print(
            f"Plants added: {len(plants)}, Total height: {sum(heights)}cm"
        )

        regular = sum(1 for p in plants if type(p) is Plant)
        flowering = sum(
            1
            for p in plants
            if isinstance(p, FloweringPlant)
            and not isinstance(p, PrizeFlower)
        )
        prize = sum(1 for p in plants if isinstance(p, PrizeFlower))

        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )

    @classmethod
    def create_garden_network(cls) -> str:
        return (
            "Garden network online. Total gardens managed: "
            f"{cls.total_gardens_managed}"
        )

    @staticmethod
    def score_garden(plants: list[Plant]) -> int:
        score = 0
        for p in plants:
            score += p.height_cm
            if isinstance(p, PrizeFlower):
                score += p.prize_points * 10
        return score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    mgr = GardenManager()

    alice_oak = Plant("Oak Tree", 100, 1000)
    alice_rose = FloweringPlant("Rose", 25, 30, "red")
    alice_sun = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    alice_rose.bloom()
    alice_sun.bloom()

    mgr.add_plant("Alice", alice_oak)
    mgr.add_plant("Alice", alice_rose)
    mgr.add_plant("Alice", alice_sun)

    before = [p.height_cm for p in mgr.gardens["Alice"]]
    mgr.help_all_grow("Alice", 1)
    after = [p.height_cm for p in mgr.gardens["Alice"]]

    mgr.garden_report("Alice")

    print(
        "Height validation test: "
        f"{GardenManager.GardenStats.validate_height(-1) is False}"
    )

    alice_score = GardenManager.score_garden(mgr.gardens["Alice"])

    mgr.add_garden("Bob")
    bob_score = GardenManager.score_garden(mgr.gardens["Bob"])

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(GardenManager.create_garden_network())
