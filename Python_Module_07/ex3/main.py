from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def hand_text(hand: list) -> str:
    parts = []
    for card in hand:
        parts.append(f"{card.name} ({card.cost})")
    return "[" + ", ".join(parts) + "]"


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())
    print()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    # prepare hand BEFORE printing it
    engine._ensure_starting_hand()

    print("Simulating aggressive turn...")
    print("Hand:", hand_text(engine.hand))
    print()

    turn = engine.simulate_turn()

    print("Turn execution:")
    print("Strategy:", turn["strategy"])
    print("Actions:", turn["actions"])
    print()

    print("Game Report:")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
