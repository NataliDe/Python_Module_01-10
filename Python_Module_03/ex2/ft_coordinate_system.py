"""
Game Coordinate System.

This module demonstrates working with 3D coordinates using tuples:
- parsing coordinates from strings
- calculating distance between two points in 3D space
- tuple unpacking
- basic error handling
"""

import sys
import math


def distance_3d(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    """
    Calculate the Euclidean distance between two 3D points.

    Args:
        a: First point as a tuple (x, y, z).
        b: Second point as a tuple (x, y, z).

    Returns:
        The distance between points a and b as a float.
    """
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_position(text: str) -> tuple[int, int, int]:
    """
    Parse a 3D position from a string.

    The expected format is: "x,y,z", where x, y, and z are integers.

    Args:
        text: Coordinate string to parse.

    Returns:
        A tuple of three integers (x, y, z).

    Raises:
        ValueError: If the format is invalid or values cannot be converted.
    """
    try:
        x_str, y_str, z_str = text.split(",")
    except ValueError:
        raise ValueError("Expected format: x,y,z")

    x = int(x_str)
    y = int(y_str)
    z = int(z_str)
    return (x, y, z)


def main() -> None:
    """
    Run a demonstration of the game coordinate system.

    This function:
    - creates sample 3D positions
    - calculates distances between points
    - parses coordinates from strings
    - demonstrates error handling and tuple unpacking
    """
    _ = sys.argv

    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)
    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    d = distance_3d(origin, pos)
    print(f"Distance between {origin} and {pos}: {d:.2f}")

    sample = "3,4,0"
    print(f'\nParsing coordinates: "{sample}"')
    parsed = parse_position(sample)
    print(f"Parsed position: {parsed}")
    d2 = distance_3d(origin, parsed)
    print(f"Distance between {origin} and {parsed}: {d2}")

    bad = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{bad}"')
    try:
        _ = parse_position(bad)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
