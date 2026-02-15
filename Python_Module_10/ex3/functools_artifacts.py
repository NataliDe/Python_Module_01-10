
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    if operation == "add":
        return functools.reduce(operator.add, spells)

    if operation == "multiply":
        return functools.reduce(operator.mul, spells)

    if operation == "max":
        return functools.reduce(
            lambda a, b: a if operator.gt(a, b) else b, spells)

    if operation == "min":
        return functools.reduce(
            lambda a, b: a if operator.lt(a, b) else b, spells)

    return 0


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, 50, "lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @functools.singledispatch
    def dispatch(arg):  # dija za zamowczuwanniam
        return "Unknown spell"

    @dispatch.register(int)
    def _(arg: int):
        return f"Damage spell: {arg} damage"

    @dispatch.register(str)
    def _(arg: str):
        return f"Enchantment: {arg}"

    @dispatch.register(list)
    def _(arg: list):
        return [dispatch(x) for x in arg]

    return dispatch


#  def my_base_enchantment(power: int, element: str, item: str) -> str:
#      return f"✨ Зачаровано {item}: додано {power} шкоди "
#               f"від стихії {element}!"


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


#    print("\nTesting spell dispatcher...")
#    cast_spell = spell_dispatcher()
#    print(cast_spell(100))                 # Має викликати damage
#    print(cast_spell("Invisibility"))      # Має викликати enchantment
#    print(cast_spell([50, "Haste", 20]))   # Має обробити список!
#    print("\nTesting partial enchanter...")
#    enchantment_book = partial_enchanter(my_base_enchantment)
#    apply_fire = enchantment_book["fire_enchant"]
#    print(apply_fire("Меч"))

if __name__ == "__main__":
    main()
