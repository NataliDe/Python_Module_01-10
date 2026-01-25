#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")
    print()

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print()

    mana = 6
    print(f"Playing {fire_dragon.name} with {mana} mana available:")
    print("Playable:", fire_dragon.is_playable(mana))
    print("Play result:", fire_dragon.play({}))
    print()

    print(f"{fire_dragon.name} attacks Goblin Warrior:")
    print("Attack result:", fire_dragon.attack_target("Goblin Warrior"))
    print()

    low_mana = 3
    print(f"Testing insufficient mana ({low_mana} available):")
    print("Playable:", fire_dragon.is_playable(low_mana))
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
