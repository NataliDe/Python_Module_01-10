#!/usr/bin/env python3


def count_occurrences(player_sets: dict[str, set[str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for achievements in player_sets.values():
        for ach in achievements:
            counts[ach] = counts.get(ach, 0) + 1
    return counts


def main() -> None:
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

    player_sets = {p: set(v) for p, v in players_raw.items()}

    for player, achievements in player_sets.items():
        print(f"Player {player} achievements: {achievements}")

    print("=== Achievement Analytics ===")

    all_unique = set()
    for achievements in player_sets.values():
        all_unique = all_unique.union(achievements)

    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    common = None
    for achievements in player_sets.values():
        if common is None:
            common = achievements
        else:
            common = common.intersection(achievements)

    if common is None:
        common = set()
    print(f"Common to all players: {common}")

    counts = count_occurrences(player_sets)
    rare = {ach for ach, c in counts.items() if c == 1}
    print(f"Rare achievements (1 player): {rare}")

    alice = player_sets["alice"]
    bob = player_sets["bob"]
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
