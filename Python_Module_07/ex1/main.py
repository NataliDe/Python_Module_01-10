
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal",
            2,
            "Common",
            5,
            "Permanent: +1 mana per turn",
        )
    )

    print("Deck stats:", deck.get_deck_stats())

    print()
    print("Drawing and playing cards:")
    print()
    deck.shuffle()

    game_state = {}
    while True:
        try:
            card = deck.draw_card()
        except ValueError:
            break

        info = card.get_card_info()
        print(f"Drew: {card.name} ({info.get('type')})")
        print("Play result:", card.play(game_state))
        print()

    print("Polymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()
