from ex0 import Card


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type,

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self._effect_text(),
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info

    @staticmethod
    def _validate_effect_type(effect_type: str) -> None:
        allowed = ("damage", "heal", "buff", "debuff")
        if effect_type not in allowed:
            raise ValueError("effect_type must be damage/heal/buff/debuff")

    def _effect_text(self) -> str:
        if self.effect_type == "damage":
            return "Deal 3 damage to target"
        if self.effect_type == "heal":
            return "Restore 3 health to target"
        if self.effect_type == "buff":
            return "Buff target"
        return "Debuff target"
