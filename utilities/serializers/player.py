""" Player Serializer / Deserializer """


class PlayerSerializer:

    def serialize_player(self, player):
        serialized_player = {
            'id': player.id,
            'first_name': player.first_name,
            'last_name': player.last_name,
            "date_of_birth": player.date_of_birth,
            "sex": player.sex,
            "ranking": player.ranking
        }
        return serialized_player
