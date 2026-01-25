from .elements import create_fire, create_water, create_air, create_earth


def healing_potion() -> str:
    """
    Brews a healing potion using fire and water elements.

    Returns:
        str: A message describing the brewed healing potion.
    """
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """
    Brews a strength potion using earth and fire elements.

    Returns:
        str: A message describing the brewed strength potion.
    """
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """
    Brews an invisibility potion using air and water elements.

    Returns:
        str: A message describing the brewed invisibility potion.
    """
    return (
        f"Invisibility potion brewed with {create_air()} "
        f"and {create_water()}"
    )


def wisdom_potion() -> str:
    """
    Brews a wisdom potion using all available elements.

    Returns:
        str: A message describing the brewed wisdom potion.
    """
    return (
        f"Wisdom potion brewed with all elements: "
        f"{create_fire()}, {create_water()}, "
        f"{create_air()} and {create_earth()}"
    )
