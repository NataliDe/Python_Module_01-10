from typing import Any, Tuple


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args) -> Tuple[Any, Any]:
        return (spell1(*args), spell2(*args))

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args) -> Any:
        return base_spell(*args) * multiplier

    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args) -> Any:
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args) -> list[Any]:
        results: list[Any] = []
        for s in spells:
            results.append(s(*args))
        return results

    return sequence


def fireball(target: str) -> str:
    return "Fireball hits " + target


def heal(target: str) -> str:
    return "Heals " + target


def fireball_damage(target: str) -> int:
    # target is accepted to match the same call style;
    # value is numeric for amplifier demo
    return 10


def is_dragon(target: str) -> bool:
    return target == "Dragon"


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    test_targets = ["Dragon", "Goblin", "Wizard", "Knight"]
    result = combined(test_targets[0])
    print("Combined spell result: " + result[0] + ", " + result[1])

    print("\nTesting power amplifier...")
    test_values = [3, 15, 25, 22]
    mega_fireball = power_amplifier(fireball_damage, test_values[0])
    original = fireball_damage("Dragon")
    amplified = mega_fireball("Dragon")
    print("Original: " + str(original) + ", Amplified: " + str(amplified))

"""
    print("Testing conditional caster...")
    dragon_only_fireball = conditional_caster(is_dragon, fireball)
    print(dragon_only_fireball("Dragon"))  # cast
    print(dragon_only_fireball("Goblin"))  # fizzled

    print("Testing spell sequence...")
    combo = spell_sequence([fireball, heal])
    print(combo("Wizard"))
"""