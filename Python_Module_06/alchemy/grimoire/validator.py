def validate_ingredients(ingredients: str) -> str:
    """
    Validates whether all given ingredients are valid elemental components.
    """
    valid_ingredients = {"fire", "water", "earth", "air"}
    items = ingredients.split()

    if all(item in valid_ingredients for item in items):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
