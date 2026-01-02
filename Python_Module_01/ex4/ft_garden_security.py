"""
Exercise 4: Garden Security System (ft_garden_security)

A secure plant model that protects internal data from corruption by using
controlled setter/getter methods with validation.
"""


class SecurePlant:
    """Represent a plant with protected data and validated updates."""

    def __init__(self, name: str) -> None:
        """
        Initialize a SecurePlant.

        Args:
            name: Plant name.
        """
        self.name = name
        self._height_cm = 0
        self._age_days = 0

    def get_height(self) -> int:
        """
        Get the current plant height in centimeters.

        Returns:
            Current height in cm.
        """
        return self._height_cm

    def get_age(self) -> int:
        """
        Get the current plant age in days.

        Returns:
            Current age in days.
        """
        return self._age_days

    def set_height(self, height_cm: int) -> None:
        """
        Safely set the plant height.

        Height cannot be negative. If invalid, prints an error message and
        keeps the previous value.

        Args:
            height_cm: New height in centimeters.
        """
        if height_cm < 0:
            print(
                f"Invalid operation attempted: height {height_cm}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            return
        self._height_cm = height_cm
        print(f"Height updated: {self._height_cm}cm [OK]")

    def set_age(self, age_days: int) -> None:
        """
        Safely set the plant age.

        Age cannot be negative. If invalid, prints an error message and
        keeps the previous value.

        Args:
            age_days: New age in days.
        """
        if age_days < 0:
            print(
                f"Invalid operation attempted: age {age_days} days [REJECTED]"
            )
            print("Security: Negative age rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days [OK]")

    def summary(self) -> str:
        """
        Return a summary string for the plant.

        Returns:
            A formatted summary with name, height, and age.
        """
        return f"{self.name} ({self._height_cm}cm, {self._age_days} days)"


def test_garden_security() -> None:
    """
    Demonstrate SecurePlant behavior with valid and invalid updates.

    This function prints a small scenario showing encapsulation and validation.
    """
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)

    print(f"Current plant: {plant.summary()}")


if __name__ == "__main__":
    test_garden_security()
