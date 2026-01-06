#!/usr/bin/env python3
import sys
import math


def distance_3d(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_position(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise ValueError("Expected format: x,y,z")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main() -> None:
    _ = sys.argv

    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    d = distance_3d(origin, pos)
    print(f"Distance between {origin} and {pos}: {d:.2f}")

    sample = "3,4,0"
    print(f'Parsing coordinates: "{sample}"')
    parsed = parse_position(sample)
    print(f"Parsed position: {parsed}")
    d2 = distance_3d(origin, parsed)
    print(f"Distance between {origin} and {parsed}: {d2}")

    bad = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad}"')
    try:
        _ = parse_position(bad)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
