import random

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card that can fight and be ranked in a tournament."""

    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        rating: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.attack_power = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters competitive play",
        }

    def attack(self, target) -> dict:
        target_name = getattr(target, "name", str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "tournament",
        }

    def defend(self, incoming_damage: int) -> dict:
        block = 2
        if incoming_damage < block:
            block = incoming_damage
        taken = incoming_damage - block
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": block,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        info = self.get_rank_info()
        info["id"] = self.card_id
        info["name"] = self.name
        return info

    def duel_power(self) -> int:
        return self.attack_power + random.randint(0, 2)
