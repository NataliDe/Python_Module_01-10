"""
Achievement Tracker System.

This module demonstrates how to use sets to track and analyze
player achievements:
- unique achievements
- common achievements
- rare achievements
- comparisons between players
"""


def count_occurrences(player_sets: dict[str, set[str]]) -> dict[str, int]:
    """
    Count how many players have each achievement.

    Args:
        player_sets: Dictionary mapping player names to sets of achievements.

    Returns:
        A dictionary mapping each achievement to the number of players
        who have it.
    """
    counts: dict[str, int] = {}
    for ach_set in player_sets.values():
        for ach in ach_set:
            if ach in counts:
                counts[ach] += 1
            else:
                counts[ach] = 1
    return counts


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

    players_raw: dict[str, list[str]] = {
        "alice": ["first_kill", "level_10", "treasure_hunter", "speed_demon"],
        "bob": ["first_kill", "level_10", "boss_slayer", "collector"],
        "charlie": [
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        ],
    }

    # Convert raw lists to sets to ensure uniqueness
    player_sets: dict[str, set[str]] = {}
    for player, achievements in players_raw.items():
        player_sets[player] = set(achievements)

    # Print achievements per player
    for player, achievements in player_sets.items():
        print(f"Player {player} achievements: {achievements}")

    print("=== Achievement Analytics ===")

    # Find all unique achievements across all players
    all_unique = set()
    for achievements in player_sets.values():
        all_unique = all_unique.union(achievements)

    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    # Find achievements common to all players
    common = None
    for achievements in player_sets.values():
        if common is None:
            common = achievements
        else:
            common = common.intersection(achievements)

    if common is None:
        common = set()
    print(f"Common to all players: {common}")

    # Find rare achievements (owned by exactly one player)
    counts = count_occurrences(player_sets)
    rare = {ach for ach, c in counts.items() if c == 1}
    print(f"Rare achievements (1 player): {rare}")

    # Compare achievements between Alice and Bob
    alice = player_sets["alice"]
    bob = player_sets["bob"]

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
