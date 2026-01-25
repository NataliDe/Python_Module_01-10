from alchemy.transmutation.basic import stone_to_gem, lead_to_gold
from alchemy.transmutation import philosophers_stone, elixir_of_life
import alchemy

print("\n=== Pathway Debate Mastery ===\n")

print("Testing Absolute Imports (from basic.py):")
print(f"lead_to_gold(): {lead_to_gold()}")
print(f"stone_to_gem(): {stone_to_gem()}")
print()

print("Testing Relative Imports (from advanced.py):")
print(f"philosophers_stone(): {philosophers_stone()}")
print(f"elixir_of_life(): {elixir_of_life()}")
print()

print("Testing Package Access:")
print(
    f"alchemy.transmutation.lead_to_gold(): "
    f"{alchemy.transmutation.lead_to_gold()}"
)
print(
    f"alchemy.transmutation.philosophers_stone(): "
    f"{alchemy.transmutation.philosophers_stone()}"
)
print()

print("Both pathways work! Absolute: clear, Relative: concise")
