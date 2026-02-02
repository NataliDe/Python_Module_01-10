"""Draw the '42' pattern using fully closed cells.

A closed cell must also force neighbors to have the shared wall closed,
otherwise the encoding becomes incoherent.
"""

from __future__ import annotations

from maze.model import ALL_WALLS, DIRS, Maze


# 7x5 digits, combined into "42" => width = 5 + 1 gap + 5 = 11, height = 7
_DIGIT_4 = [
    "#   #",
    "#   #",
    "#   #",
    "#####",
    "    #",
    "    #",
    "    #",
]

_DIGIT_2 = [
    "#####",
    "    #",
    "    #",
    "#####",
    "#    ",
    "#    ",
    "#####",
]


def apply_42(maze: Maze, entry: tuple[int, int], exit_: tuple[int, int]) -> bool:
    """Try to draw a visible '42' pattern. Return True if applied, else False.

    If the maze is too small, return False (caller should print a message).
    If the centered placement overlaps entry/exit, we try a few offsets.
    """
    pattern = _compose_42()
    ph = len(pattern)
    pw = len(pattern[0])

    if maze.width < pw or maze.height < ph:
        return False

    # Candidate placements: center first, then some small offsets
    cx = (maze.width - pw) // 2
    cy = (maze.height - ph) // 2

    candidates = [
        (cx, cy),
        (cx - 1, cy),
        (cx + 1, cy),
        (cx, cy - 1),
        (cx, cy + 1),
        (cx - 2, cy),
        (cx + 2, cy),
        (cx, cy - 2),
        (cx, cy + 2),
    ]

    for ox, oy in candidates:
        if _can_place(pattern, maze, ox, oy, entry, exit_):
            _place(pattern, maze, ox, oy)
            return True

    return False


def _compose_42() -> list[str]:
    out: list[str] = []
    for r in range(len(_DIGIT_4)):
        out.append(_DIGIT_4[r] + " " + _DIGIT_2[r])
    return out


def _can_place(
    pattern: list[str],
    maze: Maze,
    ox: int,
    oy: int,
    entry: tuple[int, int],
    exit_: tuple[int, int],
) -> bool:
    ph = len(pattern)
    pw = len(pattern[0])

    if ox < 0 or oy < 0 or (ox + pw) > maze.width or (oy + ph) > maze.height:
        return False

    ex, ey = entry
    xx, xy = exit_

    for py in range(ph):
        for px in range(pw):
            if pattern[py][px] != "#":
                continue
            x = ox + px
            y = oy + py
            if (x, y) == (ex, ey) or (x, y) == (xx, xy):
                return False

    return True


def _place(pattern: list[str], maze: Maze, ox: int, oy: int) -> None:
    """Place pattern by closing cells and forcing neighbor shared walls closed."""
    ph = len(pattern)
    pw = len(pattern[0])

    for py in range(ph):
        for px in range(pw):
            if pattern[py][px] != "#":
                continue

            x = ox + px
            y = oy + py

            # Close this cell completely
            maze.walls[y][x] = ALL_WALLS

            # Force neighbors to have shared wall closed too
            for _, dx, dy, wall_here, wall_there in DIRS:
                nx = x + dx
                ny = y + dy
                if not maze.in_bounds(nx, ny):
                    continue
                # this cell must have wall_here closed (already true),
                # neighbor must have wall_there closed:
                maze.walls[ny][nx] |= wall_there
