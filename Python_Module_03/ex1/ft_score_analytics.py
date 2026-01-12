"""
Player Score Analytics.

This module analyzes player scores provided via command-line arguments.
It demonstrates:
- parsing numeric input safely
- basic list processing
- simple statistical calculations
"""

import sys


def parse_scores(argv: list[str]) -> list[int]:
    """
    Parse command-line arguments into a list of integer scores.

    Each argument is converted to an integer. Invalid values are ignored
    with an informative message.

    Args:
        argv: List of strings representing command-line arguments.

    Returns:
        A list of valid integer scores.
    """
    scores: list[int] = []
    for arg in argv:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score ignored: {arg}")
    return scores


def main() -> None:
    """
    Run the player score analytics program.

    This function:
    - reads scores from command-line arguments
    - validates input
    - computes basic statistics (total, average, min, max, range)
    - prints the results
    """
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores = parse_scores(sys.argv[1:])

    if not scores:
        print(
            "No valid scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
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
