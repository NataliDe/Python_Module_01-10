
from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract magic interface."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on targets."""

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana into internal pool."""

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return magic stats."""
