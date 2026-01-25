from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name: str):
        if name == "Goblin Warrior":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name: str):
        if name == "Fireball":
            return SpellCard("Fireball", 4, "Uncommon", "damage")
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name: str):
        if name == "Mana Ring":
            return ArtifactCard(
                "Mana Ring",
                3,
                "Uncommon",
                3,
                "Permanent: Cards cost 1 less mana",
            )
        return ArtifactCard(
            "Mana Crystal",
            2,
            "Common",
            5,
            "Permanent: +1 mana per turn",
        )

    def create_themed_deck(self, size: int):
        deck = []

        if size >= 1:
            deck.append(self.create_creature("Fire Dragon"))
        if size >= 2:
            deck.append(self.create_creature("Goblin Warrior"))
        if size >= 3:
            deck.append(self.create_spell("Lightning Bolt"))

        while len(deck) < size:
            deck.append(self.create_artifact("Mana Ring"))

        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
