from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """
    Transmutes lead into gold using the fire element.

    Returns:
        str: A message describing the lead-to-gold transmutation.
    """
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """
    Transmutes stone into a gem using the earth element.

    Returns:
        str: A message describing the stone-to-gem transmutation.
    """
    return f"Stone transmuted to gem using {create_earth()}"
