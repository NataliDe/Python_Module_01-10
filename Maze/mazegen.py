"""
mazegen.py

Reusable maze generator module (single file).

Features:
- Maze structure with 4-bit wall encoding per cell (N/E/S/W)
- DFS / recursive backtracker generator (perfect maze when perfect=True)
- BFS shortest path that returns a direction string made of N/E/S/W

Usage example:
    from mazegen import MazeGenerator, shortest_path_dirs

    gen = MazeGenerator(width=20, height=15, seed=42, perfect=True)
    maze = gen.generate(entry=(0, 0))
    path = shortest_path_dirs(maze, start=(0, 0), goal=(19, 14))
    print(path)

Wall encoding (1 means CLOSED):
- bit0: North
- bit1: East
- bit2: South
- bit3: West
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import deque
import random
from typing import Deque


class MazeGenError(Exception):
    """Base error for mazegen module."""


NORTH = 1  # 0001
EAST = 2   # 0010
SOUTH = 4  # 0100
WEST = 8   # 1000
ALL_WALLS = NORTH | EAST | SOUTH | WEST

# (letter, dx, dy, wall_on_current, wall_on_neighbor)
DIRS: list[tuple[str, int, int, int, int]] = [
    ("N", 0, -1, NORTH, SOUTH),
    ("E", 1, 0, EAST, WEST),
    ("S", 0, 1, SOUTH, NORTH),
    ("W", -1, 0, WEST, EAST),
]


@dataclass
class Maze:
    """Maze grid where walls[y][x] is an int 0..15 (4 wall bits)."""
    width: int
    height: int
    walls: list[list[int]]

    @classmethod
    def with_all_walls(cls, width: int, height: int) -> "Maze":
        return cls(
            width=width,
            height=height,
            walls=[[ALL_WALLS for _ in range(width)] for _ in range(height)],
        )

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        out: list[tuple[int, int]] = []
        for _, dx, dy, _, _ in DIRS:
            nx = x + dx
            ny = y + dy
            if self.in_bounds(nx, ny):
                out.append((nx, ny))
        return out

    def open_between(self, x: int, y: int, nx: int, ny: int) -> None:
        dx = nx - x
        dy = ny - y
        for _, vx, vy, wall_here, wall_there in DIRS:
            if dx == vx and dy == vy:
                self.walls[y][x] &= ~wall_here
                self.walls[ny][nx] &= ~wall_there
                return
        raise MazeGenError("open_between: cells are not neighbors")

    def can_move(self, x: int, y: int, nx: int, ny: int) -> bool:
        dx = nx - x
        dy = ny - y
        v = self.walls[y][x]
        for _, vx, vy, wall_here, _ in DIRS:
            if dx == vx and dy == vy:
                return (v & wall_here) == 0
        return False


class MazeGenerator:
    """Maze generator with seeded randomness."""

    def __init__(self, width: int, height: int, seed: int, perfect: bool = True) -> None:
        if width <= 0 or height <= 0:
            raise MazeGenError("width and height must be > 0")
        self.width = width
        self.height = height
        self.seed = seed
        self.perfect = perfect
        self._rng = random.Random(seed)

    def generate(self, entry: tuple[int, int]) -> Maze:
        maze = Maze.with_all_walls(self.width, self.height)
        ex, ey = entry
        if not maze.in_bounds(ex, ey):
            raise MazeGenError("entry out of bounds")

        visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        stack: list[tuple[int, int]] = [(ex, ey)]
        visited[ey][ex] = True

        while stack:
            x, y = stack[-1]
            unvisited = [(nx, ny) for (nx, ny) in maze.neighbors(x, y)
                         if not visited[ny][nx]]
            if not unvisited:
                stack.pop()
                continue

            nx, ny = self._rng.choice(unvisited)
            maze.open_between(x, y, nx, ny)
            visited[ny][nx] = True
            stack.append((nx, ny))

        if not self.perfect:
            self._add_some_cycles(maze)

        return maze

    def _add_some_cycles(self, maze: Maze) -> None:
        target = max(1, (self.width * self.height) // 20)
        opened = 0
        attempts = 0
        max_attempts = target * 50

        while opened < target and attempts < max_attempts:
            attempts += 1
            x = self._rng.randrange(self.width)
            y = self._rng.randrange(self.height)
            neigh = maze.neighbors(x, y)
            if not neigh:
                continue
            nx, ny = self._rng.choice(neigh)
            if maze.can_move(x, y, nx, ny):
                continue
            if self._would_be_too_open(maze, x, y, nx, ny):
                continue
            maze.open_between(x, y, nx, ny)
            opened += 1

    @staticmethod
    def _open_degree(val: int) -> int:
        closed = 0
        for mask in (NORTH, EAST, SOUTH, WEST):
            if val & mask:
                closed += 1
        return 4 - closed

    def _would_be_too_open(self, maze: Maze, x: int, y: int, nx: int, ny: int) -> bool:
        a = maze.walls[y][x]
        b = maze.walls[ny][nx]
        return (self._open_degree(a) + 1) >= 3 or (self._open_degree(b) + 1) >= 3


def shortest_path_dirs(maze: Maze, start: tuple[int, int], goal: tuple[int, int]) -> str:
    """BFS shortest path; return direction letters string (N/E/S/W)."""
    sx, sy = start
    gx, gy = goal
    if not maze.in_bounds(sx, sy) or not maze.in_bounds(gx, gy):
        raise MazeGenError("start/goal out of bounds")

    q: Deque[tuple[int, int]] = deque()
    q.append((sx, sy))
    seen = {(sx, sy)}
    prev: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}

    while q:
        x, y = q.popleft()
        if (x, y) == (gx, gy):
            return _reconstruct(prev, start, goal)

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

    raise MazeGenError("no path found")


def _reconstruct(
    prev: dict[tuple[int, int], tuple[tuple[int, int], str]],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> str:
    cur = goal
    letters: list[str] = []
    while cur != start:
        if cur not in prev:
            raise MazeGenError("reconstruct failed")
        p, letter = prev[cur]
        letters.append(letter)
        cur = p
    letters.reverse()
    return "".join(letters)
