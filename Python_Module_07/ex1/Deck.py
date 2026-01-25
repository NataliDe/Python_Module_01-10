import random

from ex0.Card import Card


class Deck:
    """Deck that can hold any Card subtype."""
    def __init__(self):
        self._cards: list[Card] = []

    def add_card(self, card: Card):
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if not self._cards:
            raise ValueError("Cannot draw from an empty deck")
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self._cards)
        avg = 0.0
        if total > 0:
            avg = sum(card.cost for card in self._cards) / total
        creatures = 0
        spells = 0
        artifacts = 0

        for card in self._cards:
            ctype = card.get_card_info().get("type")
            if ctype == "Creature":
                creatures += 1
            elif ctype == "Spell":
                spells += 1
            elif ctype == "Artifact":
                artifacts += 1

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg, 1),
        }
