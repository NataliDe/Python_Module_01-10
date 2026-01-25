from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: list = []
        self.battlefield: list = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def _ensure_starting_hand(self) -> None:
        if self.factory is None:
            raise ValueError("Engine not configured")

        if not self.hand:
            self.hand = self.factory.create_themed_deck(3)
            self.cards_created += 3

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise ValueError("Engine not configured")

        self._ensure_starting_hand()

        actions = self.strategy.execute_turn(self.hand, self.battlefield)

        self.turns_simulated += 1
        self.total_damage += actions["damage_dealt"]

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": actions,
        }

    def get_engine_status(self) -> dict:
        if self.strategy is None:
            raise ValueError("Engine not configured")

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
