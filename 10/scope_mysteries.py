
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
    # --- Extra test data (as requested) ---
    initial_powers = [70, 67, 37]
    power_additions = [10, 19, 12, 16, 18]
    enchantment_types = ["Radiant", "Windy", "Earthen"]
    items_to_enchant = ["Armor", "Sword", "Ring", "Wand"]

    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    for start in initial_powers:
        acc = spell_accumulator(start)
        print(f"\nStart power: {start}")
        for add in power_additions:
            print(f" +{add} => {acc(add)}")

    print("\nTesting enchantment factory...")
    for ench in enchantment_types:
        enchant = enchantment_factory(ench)
        for item in items_to_enchant:
            print(enchant(item))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("first_power", initial_powers[0])
    vault["store"]("last_item", items_to_enchant[-1])
    print("Recall first_power:", vault["recall"]("first_power"))
    print("Recall last_item:", vault["recall"]("last_item"))
    print("Recall missing_key:", vault["recall"]("missing_key"))
