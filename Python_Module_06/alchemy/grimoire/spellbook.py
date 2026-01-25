def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Records a spell after validating its ingredients.

    The function validates the provided ingredients and returns a message
    indicating whether the spell was recorded or rejected.

    Args:
        spell_name (str): The name of the spell to be recorded.
        ingredients (str): A space-separated list of ingredients.

    Returns:
        str: A message describing the result of the spell recording.
    """
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})"
