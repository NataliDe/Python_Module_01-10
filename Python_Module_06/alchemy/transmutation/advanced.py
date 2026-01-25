from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """
    Creates the Philosopher's Stone using alchemical transmutation
    and a healing potion.

    Returns:
        str: A message describing the creation of the Philosopher's Stone.
    """
    return (
        f"Philosopher’s stone created using "
        f"{lead_to_gold()} and {healing_potion()}"
    )


def elixir_of_life() -> str:
    """
    Creates the Elixir of Life, granting eternal youth.

    Returns:
        str: A message describing the creation of the Elixir of Life.
    """
    return ("Elixir of life: eternal youth achieved!")
