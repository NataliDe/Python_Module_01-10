class Plant:

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def summary(self) -> str:
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")
    for p in plants:
        print(f"Created: {p.summary()}")
    print(f"Total plants created: {len(plants)}")
