from ex0.Card import Card


class ArtifactCard(Card):
    """Artifact card that remains in play until destroyed."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self._validate_durability(durability)
        self._validate_effect(effect)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"artifact": self.name, "active": False}

        self.durability -= 1
        return {
            "artifact": self.name,
            "active": True,
            "durability_left": self.durability,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info

    @staticmethod
    def _validate_durability(durability: int) -> None:
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("durability must be a positive integer")

    @staticmethod
    def _validate_effect(effect: str) -> None:
        if not isinstance(effect, str) or not effect:
            raise ValueError("effect must be a non-empty string")
