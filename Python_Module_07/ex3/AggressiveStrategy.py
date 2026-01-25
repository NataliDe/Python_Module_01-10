from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_budget = 5
        mana_used = 0
        damage = 0
        cards_played = []
        targets_attacked = []

        # play cheapest first -> Goblin (2) then Bolt (3)
        sorted_hand = sorted(hand, key=lambda c: c.cost)

        for card in sorted_hand:
            if mana_used + card.cost > mana_budget:
                continue

            mana_used += card.cost
            cards_played.append(card.name)

            if isinstance(card, CreatureCard):
                battlefield.append(card)
                damage += card.attack
                targets_attacked.append("Enemy Player")

            elif isinstance(card, SpellCard):
                damage += 3
                targets_attacked.append("Enemy Player")

        # remove played cards from the real hand
        for played_name in cards_played:
            for i, c in enumerate(hand):
                if c.name == played_name:
                    hand.pop(i)
                    break

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage,
        }
