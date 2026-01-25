from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages tournament cards and matches."""

    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        p1 = card1.duel_power()
        p2 = card2.duel_power()

        if p1 >= p2:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        values = list(self.cards.values())
        values.sort(key=lambda c: c.rating, reverse=True)
        return values

    def generate_tournament_report(self) -> dict:
        total = len(self.cards)
        avg = 0
        if total > 0:
            avg = sum(c.rating for c in self.cards.values()) // total

        status = "empty"
        if total > 0:
            status = "active"

        return {
            "total_cards": total,
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": status,
        }
