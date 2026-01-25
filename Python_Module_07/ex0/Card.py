from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card into the game state."""
        pass

    def get_card_info(self) -> dict:
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Card",
        }
        )

    def is_playable(self, available_mana: int) -> bool:
        """True if available mana is enough."""
        return available_mana >= self.cost
