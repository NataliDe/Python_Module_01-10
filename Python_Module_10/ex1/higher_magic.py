
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for s in spells:
            results.append(s(*args, **kwargs))
        return results
    return sequence


def fireball(target: str) -> str:
    return "Fireball hits " + target


def heal(target: str) -> str:
    return "Heals " + target


def fireball_damage(target: str) -> int:
    #  for  demo
    return 10


def is_boss(target: str) -> bool:
    if target == "Dragon":
        return True
    else:
        return False


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print("Combined spell result: " + result[0] + ", " + result[1])

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball_damage, 3)
    original = fireball_damage("Dragon")
    amplified = mega_fireball("Dragon")
    print("Original: " + str(original) + ", Amplified: " + str(amplified))

    #  print("\nTesting conditional caster...")
    #  boss_only_fireball = conditional_caster(is_boss, fireball)
    #  print("Against Dragon: " + boss_only_fireball("Dragon"))
    #  listes = [heal, fireball]
    #  spel_s = spell_sequence(listes)
    #  print(spel_s("Dragon"))


if __name__ == "__main__":
    main()
