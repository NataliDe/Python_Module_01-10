"""
higher_magic.py (Exercise 1: Higher Realm)

Directory: ex1/
Files to Submit: higher_magic.py
Authorized: callable(), print()
"""


# Function Signatures (as required):
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Return a new spell that calls both spells with the same arguments."""
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Return a new spell that multiplies the base spell's numeric result."""
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    Return a new spell that casts only if condition(*args, **kwargs) is True.
    If condition fails, return "Spell fizzled".
    """
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """Return a new spell that casts all spells in
    order and returns list of results."""
    def sequence(*args, **kwargs):
        results = []
        for s in spells:
            results.append(s(*args, **kwargs))
        return results
    return sequence


# --- Demo spells for testing ---
def fireball(target: str) -> str:
    return "Fireball hits " + target


def heal(target: str) -> str:
    return "Heals " + target


def fireball_damage(target: str) -> int:
    # target is accepted to match the same call style;
    # value is numeric for amplifier demo
    return 10


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print("Combined spell result: " + result[0] + ", " + result[1])

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball_damage, 3)
    original = fireball_damage("Dragon")
    amplified = mega_fireball("Dragon")
    print("Original: " + str(original) + ", Amplified: " + str(amplified))


if __name__ == "__main__":
    main()
