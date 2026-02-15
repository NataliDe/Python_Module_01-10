def mage_counter() -> callable:

    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:

    total = initial_power

    def add_power(amount: int) -> int:
        nonlocal total
        try:
            total += amount
        except TypeError:
            # isn't a number
            return total
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchant(item_name: str) -> str:
        try:
            return f"{enchantment_type} {item_name}"
        except Exception:
            return "Enchantment failed"

    return enchant


def memory_vault() -> dict[str, callable]:

    storage: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        try:
            storage[key] = value
        except Exception:
            # nothing
            return

    def recall(key: str) -> object:
        try:
            return storage[key]
        except KeyError:
            return "Memory not found"
        except Exception:
            return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    #  power_new = spell_accumulator(12)
    #  power_res = power_new(3)
    #  print(f"Toatl is {power_res}")

    #  vault = memory_vault()
    #  save_spell = vault["store"]
    #  get_spell = vault["recall"]
    #  save_spell("fireball", "Opis fireball")
    #  print(get_spell("fireball"))
