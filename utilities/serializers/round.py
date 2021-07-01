"""Round Serializer /Deserializer"""


class RoundSerializer:

    def serialize_round(self, round: object) -> dict:
        match_list_id = []
        for match in round.matchs:
            match_list_id.append(match.id)

        serialized_round = {
            'id': round.id,
            'round_name': round.round_name,
            'start_round_datetime': str(round.start_round_datetime),
            'end_round_datetime': str(round.end_round_datetime),
            'matchs': match_list_id
        }
        return serialized_round
