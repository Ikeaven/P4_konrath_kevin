"""Match Serializer / Deserializer."""


class MatchSerializer:

    def serialize_matchs(self, match: object) -> dict:
        serialized_matchs = {
            'id': match.id,
            'player1': match.player1.id,
            'score_player1': match.score_player1,
            'player2': match.player2.id,
            'score_player2': match.score_player2
        }
        return serialized_matchs
