#!/usr/bin/env python3
import sys


def parse_scores(argv: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in argv:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score ignored: {arg}")
    return scores


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = parse_scores(sys.argv[1:])

    if not scores:
        print("No valid scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average = total_score / total_players
    high = max(scores)
    low = min(scores)
    score_range = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
