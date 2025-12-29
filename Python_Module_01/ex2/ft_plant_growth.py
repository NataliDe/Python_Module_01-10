class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm: int = 1) -> None:
        self.height_cm += cm

    def age(self, days: int = 1) -> None:
        self.age_days += days

    def get_info(self) -> str:
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


if __name__ == "__main__":
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
