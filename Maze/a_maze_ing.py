#!/usr/bin/env python3
"""a_maze_ing.py

Usage:
    python3 a_maze_ing.py config.txt
"""

from __future__ import annotations
from maze.pattern_42 import apply_42
from maze.errors import MazeError


import sys

from maze.config import ConfigError, load_config
from maze.generator import MazeGenerator
from maze.render_ascii import AsciiRenderer
from maze.solver import shortest_path_dirs
from maze.writer import write_output


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} config.txt")
        return 1

    try:
        cfg = load_config(sys.argv[1])
    except ConfigError as exc:
        print(f"Config error: {exc}")
        return 1

    state = {
        "seed": cfg.seed,
        "maze": None,
        "path": "",
    }

    def build(regenerate: bool = False):
        if regenerate:
            state["seed"] = int(state["seed"]) + 1

        gen = MazeGenerator(cfg.width, cfg.height, int(state["seed"]), cfg.perfect)
        maze = gen.generate(cfg.entry)

        # --- try to apply "42" pattern (allowed to skip if too small) ---
        backup = [row[:] for row in maze.walls]
        applied = apply_42(maze, cfg.entry, cfg.exit)
        if not applied:
            print("Warning: maze too small (or no safe spot) to draw '42' pattern.")
        else:
            # Make sure entry->exit still has a path; if not, revert the pattern
            try:
                _ = shortest_path_dirs(maze, cfg.entry, cfg.exit)
            except MazeError:
                maze.walls = backup
                print("Warning: '42' pattern blocked the solution path, skipped.")

        path = shortest_path_dirs(maze, cfg.entry, cfg.exit)

        state["maze"] = maze
        state["path"] = path

        write_output(
            maze=maze,
            output_file=cfg.output_file,
            entry=cfg.entry,
            exit_=cfg.exit,
            path_dirs=path,
        )
        return maze, cfg.entry, cfg.exit, path, int(state["seed"])


    # initial build
    build(regenerate=False)

    renderer = AsciiRenderer()

    def get_state(regenerate: bool = False):
        return build(regenerate=regenerate)

    renderer.run(get_state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
