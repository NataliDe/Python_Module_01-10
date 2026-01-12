#!/usr/bin/env python3
"""
ft_analytics_dashboard.py

Authorized:
- List/dict/set comprehensions
- len(), print(), sum(), max(), min(), sorted()

Goal:
Demonstrate comprehension mastery by transforming simple, hardcoded
gaming data into useful analytics.
"""


def category(score: int) -> str:
    """Return a score category label for a numeric score."""
    if score >= 2000:
        return "high"
    if score >= 1000:
        return "medium"
    return "low"


def main() -> None:
    """Run the analytics dashboard demo."""
    print("=== Game Analytics Dashboard ===")

    # --- Sample data (hardcoded, simple) ---
    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }
    active_players = ["alice", "bob", "charlie"]
    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north",
    }
    achievements = {
        "alice": [
            "first_kill",
            "level_10", "boss_slayer", "treasure_hunter", "speed"
            ],
        "bob": ["first_kill", "level_10", "collector"],
        "charlie": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "perfectionist",
            "speed",
            "explorer",
            "builder",
        ],
        "diana": ["first_kill", "boss_slayer", "speed", "explorer"],
    }

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p for p, s in scores.items() if s > 2000]
    scores_doubled = [s * 2 for s in scores.values()]
    active = [p for p in active_players if p in scores]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p: s for p, s in scores.items() if p in active_players}
    score_categories = {}
    for k in {"high", "medium", "low"}:
        count = 0
        for s in scores.values():
            if category(s) == k:
                count += 1
        score_categories[k] = count
    achievement_counts = {p: len(a) for p, a in achievements.items()}

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    # set comprehension !! OMG
    unique_players = {p for p in scores.keys()}
    # dla koznogo spysku ach, dla koznogo ach dodaj do a
    unique_achievements = {
                    a for ach_list in achievements.values()
                    for a in ach_list}
    active_regions = {regions[p] for p in active_players}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(unique_players)
    total_unique_ach = len(unique_achievements)

    all_scores = [s for s in scores.values()]
    avg_score = sum(all_scores) / len(all_scores)

    top_player = max(scores, key=scores.get)
    top_score = scores[top_player]
    top_ach = achievement_counts[top_player]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: "
          f"{top_player} ({top_score} points, {top_ach} achievements)")


if __name__ == "__main__":
    main()
