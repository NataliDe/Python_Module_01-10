"""Maze generation algorithms (MVP: DFS recursive backtracker)."""

from __future__ import annotations

import random

from maze.errors import MazeError
from maze.model import Maze


class MazeGenerator:
    """Generate mazes with a fixed seed (reproducible)."""

    def __init__(self, width: int, height: int, seed: int, perfect: bool) -> None:
        self.width = width
        self.height = height
        self.seed = seed
        self.perfect = perfect
        self._rng = random.Random(seed)

    def generate(self, start: tuple[int, int]) -> Maze:
        if self.width <= 0 or self.height <= 0:
            raise MazeError("Invalid maze size")

        maze = Maze.with_all_walls(self.width, self.height)

        sx, sy = start
        if not maze.in_bounds(sx, sy):
            raise MazeError("Start is out of bounds")

        visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        stack: list[tuple[int, int]] = [(sx, sy)]
        visited[sy][sx] = True

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

        # If perfect=False, we can add extra openings (cycles).
        # NOTE: The "no large open areas" rule is complex; here we add a small number
        # of random openings with a conservative local check.
        if not self.perfect:
            self._add_some_cycles(maze)

        return maze

    def _add_some_cycles(self, maze: Maze) -> None:
        """Open a few extra walls to create loops (imperfect maze).

        Conservative approach: open only a limited number of edges and avoid
        opening if it would make a cell too 'open' (>=3 open sides).
        """
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
    def _open_degree(walls_value: int) -> int:
        """How many open sides does a cell have?"""
        # 4 sides total; closed sides are bits=1
        closed = 0
        for mask in (1, 2, 4, 8):
            if walls_value & mask:
                closed += 1
        return 4 - closed

    def _would_be_too_open(self, maze: Maze, x: int, y: int, nx: int, ny: int) -> bool:
        """Prevent opening if it would make either endpoint have >=3 open sides."""
        a = maze.walls[y][x]
        b = maze.walls[ny][nx]
        deg_a = self._open_degree(a)
        deg_b = self._open_degree(b)
        # opening adds 1 open side to each endpoint
        return (deg_a + 1) >= 3 or (deg_b + 1) >= 3
