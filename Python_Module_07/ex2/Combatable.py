
from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract combat interface."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Attack a target."""

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against damage."""

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return combat stats."""
