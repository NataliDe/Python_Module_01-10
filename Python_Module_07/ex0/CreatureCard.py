from ex0.Card import Card


class CreatureCard(Card):
    """Creature card with combat stats."""
    def __init__(self,
                 name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("attack must be a positive integer")
        if health <= 0:
            raise ValueError("health must be a positive integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        target_name = getattr(target, "name", None)
        if target_name is None:
            target_name = str(target)

        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
