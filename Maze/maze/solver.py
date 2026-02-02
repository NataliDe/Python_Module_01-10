"""Shortest path solver (BFS)."""

from __future__ import annotations

from collections import deque

from maze.errors import MazeError
from maze.model import DIRS, Maze


def shortest_path_dirs(
    maze: Maze,
    start: tuple[int, int],
    goal: tuple[int, int],
) -> str:
    sx, sy = start
    gx, gy = goal

    if not maze.in_bounds(sx, sy) or not maze.in_bounds(gx, gy):
        raise MazeError("Start or goal out of bounds")

    q: deque[tuple[int, int]] = deque()
    q.append((sx, sy))

    prev: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}
    seen = {(sx, sy)}

    while q:
        x, y = q.popleft()
        if (x, y) == (gx, gy):
            return _reconstruct(prev, (sx, sy), (gx, gy))

        for letter, dx, dy, _, _ in DIRS:
            nx = x + dx
            ny = y + dy
            if not maze.in_bounds(nx, ny):
                continue
            if (nx, ny) in seen:
                continue
            if not maze.can_move(x, y, nx, ny):
                continue

            seen.add((nx, ny))
            prev[(nx, ny)] = ((x, y), letter)
            q.append((nx, ny))

    raise MazeError("No path found (maze may be invalid)")


def _reconstruct(
    prev: dict[tuple[int, int], tuple[tuple[int, int], str]],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> str:
    cur = goal
    letters: list[str] = []
    while cur != start:
        if cur not in prev:
            raise MazeError("Path reconstruction failed")
        p, letter = prev[cur]
        letters.append(letter)
        cur = p
    letters.reverse()
    return "".join(letters)
