"""Terminal ASCII renderer with simple interactions."""

from __future__ import annotations

from maze.model import ALL_WALLS, EAST, NORTH, SOUTH, WEST, Maze


class AsciiRenderer:
    def __init__(self) -> None:
        self.show_path = True

    def run(
        self,
        get_state,  # callable returning (maze, entry, exit, path_dirs, seed)
    ) -> None:
        """Interactive loop: p toggle path, r regenerate, q quit."""
        while True:
            maze, entry, exit_, path_dirs, seed = get_state()
            print()
            print(f"Seed: {seed}")
            print(self.render(maze, entry, exit_, path_dirs if self.show_path else ""))
            cmd = input("[p]ath toggle | [r]egen | [q]uit > ").strip().lower()
            if cmd == "q":
                return
            if cmd == "p":
                self.show_path = not self.show_path
            elif cmd == "r":
                # caller should update seed/state
                get_state(regenerate=True)  # type: ignore[misc]
            else:
                print("Unknown command.")

    def render(
        self,
        maze: Maze,
        entry: tuple[int, int],
        exit_: tuple[int, int],
        path_dirs: str,
    ) -> str:
        h = maze.height
        w = maze.width
        grid_h = 2 * h + 1
        grid_w = 2 * w + 1

        canvas = [["#" for _ in range(grid_w)] for _ in range(grid_h)]

        # carve spaces
        for y in range(h):
            for x in range(w):
                cy = 2 * y + 1
                cx = 2 * x + 1
                canvas[cy][cx] = " "

                v = maze.walls[y][x]
                if (v & NORTH) == 0:
                    canvas[cy - 1][cx] = " "
                if (v & SOUTH) == 0:
                    canvas[cy + 1][cx] = " "
                if (v & WEST) == 0:
                    canvas[cy][cx - 1] = " "
                if (v & EAST) == 0:
                    canvas[cy][cx + 1] = " "

        # draw entry/exit
        ex, ey = entry
        xx, xy = exit_
        canvas[2 * ey + 1][2 * ex + 1] = "E"
        canvas[2 * xy + 1][2 * xx + 1] = "X"

        # optional path overlay
        if path_dirs:
            x, y = entry
            for ch in path_dirs:
                if ch == "N":
                    y -= 1
                elif ch == "S":
                    y += 1
                elif ch == "E":
                    x += 1
                elif ch == "W":
                    x -= 1
                cy = 2 * y + 1
                cx = 2 * x + 1
                if (x, y) != entry and (x, y) != exit_:
                    canvas[cy][cx] = "·"

        return "\n".join("".join(row) for row in canvas)
