#!/usr/bin/env python3


def category(score: int) -> str:
    if score > 2000:
        return "high"
    if score >= 1200:
        return "medium"
    return "low"


def main() -> None:
    print("=== Game Analytics Dashboard ===")

    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }

    achievements = {
        "alice": {
            "first_kill",
            "level_10",
            "boss_slayer",
            "explorer",
            "collector"
            },
        "bob": {"first_kill", "level_10", "explorer"},
        "charlie": {
            "level_10",
            "boss_slayer",
            "treasure_hunter",
            "speed_demon",
            "explorer",
            "strategist",
            "perfectionist",
        },
        "diana": {"first_kill", "level_10", "treasure_hunter", "explorer"},
    }

    active_players = {"alice", "bob", "charlie"}
    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north"
        }

    print("=== Dict Comprehension Examples ===")

    player_scores = {
        player: score
        for player, score in scores.items()
        if player in active_players
    }

    categories = {"high", "medium", "low"}
    cats = {}

    for cat in categories:
        count = 0
        for score in scores.values():
            if category(score) == cat:
                count += 1
        cats[cat] = count

    ach_counts = {
        player: len(achs)
        for player, achs in achievements.items()
    }

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {cats}")
    print(f"Achievement counts: {ach_counts}")

    print("=== Set Comprehension Examples ===")
    unique_players = {p for p in scores.keys()}
    unique_ach = {a for aset in achievements.values() for a in aset}
    active_regions = {regions[p] for p in active_players}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {active_regions}")

    print("=== Combined Analysis ===")
    total_players = len(scores)
    total_unique_ach = len(unique_ach)
    avg_score = sum(scores.values()) / len(scores)
    top_player = max(scores, key=lambda k: scores[k])
    top_score = scores[top_player]
    top_ach = len(achievements.get(top_player, set()))

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_player} ({top_score} points, "
          f"{top_ach} achievements)")


if __name__ == "__main__":
    main()
