
from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    elite = EliteCard("Arcane Warrior", 5, "Rare", 5, 5)

    print("EliteCard capabilities:")
    print("- Card:", ["play", "get_card_info", "is_playable"])
    print("- Combatable:", ["attack", "defend", "get_combat_stats"])
    print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])

    print()
    print(f"Playing {elite.name} (Elite Card):")
    print()
    print("Combat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(5))
    print()

    print("Magic phase:")
    elite.channel_mana(8)
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", elite.channel_mana(3))
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
