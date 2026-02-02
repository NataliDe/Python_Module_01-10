"""Maze data model and wall bit encoding.

Bits (1 means wall CLOSED, 0 means OPEN):
- bit0: North
- bit1: East
- bit2: South
- bit3: West
"""

from __future__ import annotations

from dataclasses import dataclass

NORTH = 1  # 0001
EAST = 2   # 0010
SOUTH = 4  # 0100
WEST = 8   # 1000

ALL_WALLS = NORTH | EAST | SOUTH | WEST

DIRS: list[tuple[str, int, int, int, int]] = [
    ("N", 0, -1, NORTH, SOUTH),
    ("E", 1, 0, EAST, WEST),
    ("S", 0, 1, SOUTH, NORTH),
    ("W", -1, 0, WEST, EAST),
]


@dataclass
class Maze:
    width: int
    height: int
    walls: list[list[int]]  # [y][x] -> 0..15

    @classmethod
    def with_all_walls(cls, width: int, height: int) -> "Maze":
        return cls(width=width, height=height,
                   walls=[[ALL_WALLS for _ in range(width)] for _ in range(height)])

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def close_all(self, x: int, y: int) -> None:
        self.walls[y][x] = ALL_WALLS

    def open_between(self, x: int, y: int, nx: int, ny: int) -> None:
        """Open the wall between (x,y) and (nx,ny) if they are neighbors."""
        dx = nx - x
        dy = ny - y

        for _, vx, vy, wall_here, wall_there in DIRS:
            if dx == vx and dy == vy:
                self.walls[y][x] &= ~wall_here
                self.walls[ny][nx] &= ~wall_there
                return

        raise ValueError("Cells are not neighbors")

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        out: list[tuple[int, int]] = []
        for _, dx, dy, _, _ in DIRS:
            nx = x + dx
            ny = y + dy
            if self.in_bounds(nx, ny):
                out.append((nx, ny))
        return out

    def can_move(self, x: int, y: int, nx: int, ny: int) -> bool:
        """Return True if there is an OPEN passage between the two neighbor cells."""
        dx = nx - x
        dy = ny - y
        cell = self.walls[y][x]

        for _, vx, vy, wall_here, _ in DIRS:
            if dx == vx and dy == vy:
                return (cell & wall_here) == 0
        return False
