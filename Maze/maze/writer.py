"""Write maze to output file in the required format."""

from __future__ import annotations

from pathlib import Path

from maze.model import Maze


def write_output(
    maze: Maze,
    output_file: str,
    entry: tuple[int, int],
    exit_: tuple[int, int],
    path_dirs: str,
) -> None:
    p = Path(output_file)
    lines: list[str] = []

    for y in range(maze.height):
        row = "".join(format(maze.walls[y][x], "X") for x in range(maze.width))
        lines.append(row)

    lines.append("")  # empty line

    ex, ey = entry
    xx, xy = exit_
    lines.append(f"{ex},{ey}")
    lines.append(f"{xx},{xy}")
    lines.append(path_dirs)

    data = "\n".join(lines) + "\n"
    p.write_text(data, encoding="utf-8")
