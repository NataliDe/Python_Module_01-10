def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(
            artifacts, key=lambda w: w.get("power", 0), reverse=True,)
    except (TypeError, AttributeError):
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(
            filter(
                lambda m: int(m.get("power", 0)) >= min_power, mages,
                # filter(function, iterable from) повертає True/False
            )
        )
    except (TypeError, ValueError, AttributeError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(
            map(lambda s: f"* {s} *", spells)
        )
    except TypeError:
        return []


def mage_stats(mages: list[dict]) -> dict:
    try:
        if not mages:
            return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

        strongest = max(mages, key=lambda m: m.get("power", 0))
        weakest = min(mages, key=lambda m: m.get("power", 0))

        max_power = int(strongest.get("power", 0))
        min_power = int(weakest.get("power", 0))

        total_power = sum(map(lambda m: int(m.get("power", 0)), mages))
        avg_power = round(total_power / len(mages), 2)

        return {
            'max_power': int(max_power),
            'min_power': int(min_power),
            'avg_power': float(avg_power),
        }
    except (TypeError, ValueError, ZeroDivisionError, ArithmeticError):
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}


if __name__ == "__main__":
    print("\nTesting artifact sorter...")

    artifacts_list = [
        {'name': 'Lightning Rod', 'power': 70, 'type': 'armor'},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {'name': 'Wind Cloak', 'power': 16, 'type': 'accessory'},
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {'name': 'Crystal Orb', 'power': 80, 'type': 'weapon'},
        {'name': 'Earth Shield', 'power': 66, 'type': 'armor'},
                 ]

    sorted_artifacts = artifact_sorter(artifacts_list)
    if len(sorted_artifacts) >= 2:
        first = sorted_artifacts[0]
        second = sorted_artifacts[1]
        print(
            f"{(first.get('name'))} ({first.get('power')} power) "
            f"comes before {(second.get('name'))} "
            f"({second.get('power')} power)"
        )

    mages = [
        {'name': 'Sage', 'power': 80, 'element': 'water'},
        {'name': 'Luna', 'power': 54, 'element': 'earth'},
        {'name': 'Ash', 'power': 70, 'element': 'wind'},
        {'name': 'Sage', 'power': 58, 'element': 'earth'},
        {'name': 'Nova', 'power': 76, 'element': 'shadow'},
        ]
    min_power = 70
    filtered_mages = power_filter(mages, min_power)

    spells = ["fireball", "heal", "shield"]

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(' '.join(transformed_spells))
