
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Elite card with both combat and magic abilities."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self._validate_stats(attack, health)
        self.attack_power = attack
        self.health = health
        self.mana_pool = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed with multiple abilities",
        }

    def attack(self, target) -> dict:
        target_name = getattr(target, "name", None)  # Якщо у target є name
        if target_name is None:
            target_name = str(target)

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            incoming_damage = 0

        blocked = 3
        if incoming_damage < blocked:
            blocked = incoming_damage

        taken = incoming_damage - blocked
        self.health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not isinstance(spell_name, str) or not spell_name:
            raise ValueError("spell_name must be a non-empty string")

        mana_used = 4
        if self.mana_pool < mana_used:
            mana_used = self.mana_pool

        self.mana_pool -= mana_used

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int) or amount < 0:
            amount = 0

        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict:
        return {"mana_pool": self.mana_pool}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Elite"
        info["attack"] = self.attack_power
        info["health"] = self.health
        return info

    @staticmethod
    def _validate_stats(attack: int, health: int) -> None:
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
