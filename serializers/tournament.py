""" Tournoi serializer / Deserializer """


class TournamentSerializer:

    def serialize_tournament(self, tournament):
        list_players_id = []
        for player in tournament.players_list:
            list_players_id.append(player.id)

        list_rounds_id = []
        for round in tournament.round_list:
            list_rounds_id.append(round.id)

        serialized_tournament = {
            'id': tournament.id,
            'tournament_name': tournament.tournament_name,
            'location': tournament.location,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'tour_number': tournament.tour_number,
            'time_controller': tournament.time_controller,
            'number_of_players': tournament.number_of_players,
            'description': tournament.description,
            'players_list': list_players_id,
            'round_list': list_rounds_id
        }
        return serialized_tournament
