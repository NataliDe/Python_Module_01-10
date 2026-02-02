"""Config parsing and validation.

Config format:
- One KEY=VALUE per line
- Lines starting with # are comments and ignored
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from maze.errors import ConfigError


def _parse_bool(value: str) -> bool:
    v = value.strip().lower()
    if v in {"true", "1", "yes", "y"}:
        return True
    if v in {"false", "0", "no", "n"}:
        return False
    raise ConfigError(f"Invalid boolean value: {value!r} (use True/False)")


def _parse_int(value: str, key: str) -> int:
    try:
        return int(value.strip())
    except ValueError as exc:
        raise ConfigError(f"Invalid integer for {key}: {value!r}") from exc


def _parse_xy(value: str, key: str) -> tuple[int, int]:
    parts = [p.strip() for p in value.split(",")]
    if len(parts) != 2:
        raise ConfigError(f"Invalid coordinates for {key}: {value!r} (use x,y)")
    x = _parse_int(parts[0], f"{key}.x")
    y = _parse_int(parts[1], f"{key}.y")
    return (x, y)


@dataclass(frozen=True)
class Config:
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int

    def validate(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ConfigError("WIDTH and HEIGHT must be > 0")

        ex, ey = self.entry
        xx, xy = self.exit

        if not (0 <= ex < self.width and 0 <= ey < self.height):
            raise ConfigError("ENTRY is out of maze bounds")

        if not (0 <= xx < self.width and 0 <= xy < self.height):
            raise ConfigError("EXIT is out of maze bounds")

        if self.entry == self.exit:
            raise ConfigError("ENTRY and EXIT must be different")

        if not self.output_file.strip():
            raise ConfigError("OUTPUT_FILE must not be empty")


REQUIRED_KEYS = {
    "WIDTH",
    "HEIGHT",
    "ENTRY",
    "EXIT",
    "OUTPUT_FILE",
    "PERFECT",
}


def load_config(path: str) -> Config:
    p = Path(path)
    if not p.exists():
        raise ConfigError(f"Config file not found: {path}")

    raw: dict[str, str] = {}

    try:
        text = p.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigError(f"Cannot read config file: {path}") from exc

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            raise ConfigError(f"Bad syntax on line {line_no}: {line!r} (missing '=')")

        key, value = stripped.split("=", 1)
        k = key.strip().upper()
        v = value.strip()
        if not k:
            raise ConfigError(f"Empty key on line {line_no}")
        raw[k] = v

    missing = sorted(REQUIRED_KEYS - set(raw.keys()))
    if missing:
        raise ConfigError(f"Missing required keys: {', '.join(missing)}")

    width = _parse_int(raw["WIDTH"], "WIDTH")
    height = _parse_int(raw["HEIGHT"], "HEIGHT")
    entry = _parse_xy(raw["ENTRY"], "ENTRY")
    exit_ = _parse_xy(raw["EXIT"], "EXIT")
    output_file = raw["OUTPUT_FILE"]
    perfect = _parse_bool(raw["PERFECT"])

    # Seed: subject says reproducibility is required, so we make it effectively required:
    if "SEED" not in raw:
        raise ConfigError("Missing required key: SEED (needed for reproducibility)")
    seed = _parse_int(raw["SEED"], "SEED")

    cfg = Config(
        width=width,
        height=height,
        entry=entry,
        exit=exit_,
        output_file=output_file,
        perfect=perfect,
        seed=seed,
    )
    cfg.validate()
    return cfg
