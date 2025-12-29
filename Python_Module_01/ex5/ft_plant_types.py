class Plant:

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def base_info(self) -> str:
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days"


class Flower(Plant):

    def __init__(
            self,
            name: str,
            height_cm: int,
            age_days: int,
            color: str,
            ) -> None:
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def info(self) -> str:
        return f"{self.base_info()}, {self.color} color"


class Tree(Plant):

    def __init__(
            self,
            name: str,
            height_cm: int,
            age_days: int,
            trunk_diameter: int,
            ) -> None:
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        return (self.trunk_diameter * self.trunk_diameter) // 32

    def info(self) -> str:
        return f"{self.base_info()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height_cm: int,
        age_days: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self) -> str:
        return f"{self.base_info()}, {self.harvest_season} harvest"


if __name__ == "__main__":
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

    for f in flowers:
        print(f"{f.name} (Flower): {f.info()}")
        f.bloom()

    for t in trees:
        shade = t.produce_shade()
        print(f"{t.name} (Tree): {t.info()}")
        print(f"{t.name} provides {shade} square meters of shade")

    for v in vegetables:
        print(f"{v.name} (Vegetable): {v.info()}")
        print(f"{v.name} is rich in {v.nutritional_value}")
