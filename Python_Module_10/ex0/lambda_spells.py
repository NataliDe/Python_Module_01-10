"""
lambda_spells.py (Exercise 0: Lambda Sanctum)

Rules (per subject):
- Use lambda expressions for all transformations.
- Use sorted() with lambda, filter() with lambda, map() with lambda.
- Provide type hints.
- No file I/O, no external libraries.
"""

from typing import Any


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort artifacts by 'power' descending using sorted() + lambda.

    Each artifact: {'name': str, 'power': int, 'type': str}
    """
    try:
        return sorted(
            artifacts,
            key=lambda a: a.get("power", 0),
            reverse=True,
        )
    except (TypeError, AttributeError):
        # If input is not a list of dict-like objects, fail gracefully.
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filter mages with power >= min_power using filter() + lambda.

    Each mage: {'name': str, 'power': int, 'element': str}
    """
    try:
        return list(
            filter(
                lambda m: int(m.get("power", 0)) >= int(min_power),
                mages,
            )
        )
    except (TypeError, ValueError, AttributeError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform spell names using map() + lambda:
    add "* " prefix and " *" suffix.
    """
    try:
        return list(map(lambda s: f"* {s} *", spells))
    except TypeError:
        return []


def mage_stats(mages: list[dict]) -> dict:
    """
    Compute max/min/avg power using max(), min(), sum() with lambda.

    Return: {'max_power': int, 'min_power': int, 'avg_power': float}
    avg rounded to 2 decimals.
    """
    try:
        if not mages:
            return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

        max_power = max(mages, key=lambda m: m.get("power", 0)).get("power", 0)
        min_power = min(mages, key=lambda m: m.get("power", 0)).get("power", 0)
        total_power = sum(map(lambda m: int(m.get("power", 0)), mages))
        avg_power = round(total_power / len(mages), 2)

        return {
            "max_power": int(max_power),
            "min_power": int(min_power),
            "avg_power": float(avg_power),
        }
    except (TypeError, ValueError, AttributeError, ZeroDivisionError):
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}


def _safe_name(obj: Any) -> str:
    """Small helper for printing (not a transformation requirement)."""
    try:
        return str(obj)
    except Exception:
        return "Unknown"


if __name__ == "__main__":
    # --- Expected Output Example-compatible demo (keep it minimal) ---
    print("Testing artifact sorter...")

    artifacts_demo = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ice Wand", "power": 70, "type": "weapon"},
    ]

    sorted_artifacts = artifact_sorter(artifacts_demo)
    if len(sorted_artifacts) >= 2:
        first = sorted_artifacts[0]
        second = sorted_artifacts[1]
        print(
            f"{_safe_name(first.get('name'))} ({first.get('power')} power) "
            f"comes before {_safe_name(second.get('name'))} "
            f"({second.get('power')} power)"
        )

    print("Testing spell transformer...")
    spells_demo = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells_demo)
    print(" ".join(transformed))
