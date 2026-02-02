"""
scope_mysteries.py (Exercise 2: Memory Depths)

Directory: ex2/
Files to Submit: scope_mysteries.py
Authorized: nonlocal, print()
"""


def mage_counter() -> callable:
    """
    Return a function that counts how many times it has been called.
    Starts from 1 and persists between calls (closure state).
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    """
    Return a function that accumulates power over time.
    Each call adds the given amount and returns the new total.
    """
    total = initial_power

    def add_power(amount: int) -> int:
        nonlocal total
        try:
            total += amount
        except TypeError:
            # Graceful fallback if amount isn't a number
            return total
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    """
    Return a function that applies the specified enchantment to an item name.
    Format: "enchantment_type item_name" (e.g. "Flaming Sword")
    """

    def enchant(item_name: str) -> str:
        try:
            return f"{enchantment_type} {item_name}"
        except Exception:
            return "Enchantment failed"

    return enchant


def memory_vault() -> dict[str, callable]:
    """
    Return a dict with 'store' and 'recall' functions.
    Uses closure to keep private storage.
    """
    storage: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        try:
            storage[key] = value
        except Exception:
            # Do nothing (graceful)
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
    print("Testing mage counter.")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("Testing enchantment factory.")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
