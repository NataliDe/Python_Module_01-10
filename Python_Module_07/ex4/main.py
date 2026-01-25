from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print()
    print("=== DataDeck Tournament Platform ===")
    print()
    print("Registering Tournament Cards...")
    print()

    platform = TournamentPlatform()

    dragon = TournamentCard(
        "dragon_001",
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5,
        1200,
    )
    wizard = TournamentCard(
        "wizard_001",
        "Ice Wizard",
        4,
        "Rare",
        3,
        4,
        1150,
    )

    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", dragon.rating)
    print(f"- Record: {dragon.wins}-{dragon.losses}")
    print()

    print(f"{wizard.name} (ID: {wizard.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", wizard.rating)
    print(f"- Record: {wizard.wins}-{wizard.losses}")
    print()

    print("Creating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        record = f"{card.wins}-{card.losses}"
        print(f"{i}. {card.name} - Rating: {card.rating} ({record})")
    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
