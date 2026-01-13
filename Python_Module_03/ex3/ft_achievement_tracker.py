"""
Achievement Tracker System.

This module demonstrates how to use sets to track and analyze
player achievements:
- unique achievements
- common achievements
- rare achievements
- comparisons between players
"""


def main() -> None:
    """
    Run the achievement tracker demo.

    This function:
    - builds player achievement sets
    - prints per-player achievements
    - analyzes unique, common, and rare achievements
    - compares achievements between players
    """
    print("=== Achievement Tracker System ===")

    # Achievements for each player
    alice = set([
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    ])

    bob = set([
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    ])

    charlie = set([
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    ])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("=== Achievement Analytics ===")

    # All unique achievements
    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    # Common achievements (shared by all players)
    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    # Rare achievements (only one player has them)
    rare = set()

    for achievement in all_achievements:
        count = 0
        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1
        if count == 1:
            rare.add(achievement)

    print(f"Rare achievements (1 player): {rare}")

    # Player comparisons
    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
