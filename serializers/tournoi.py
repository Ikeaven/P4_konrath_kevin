""" Tournoi serializer / Deserializer """


class TournamentSerializer:

    def serialize_tournament(self, tournament):
        serialized_tournament = {
            'tournament_name': tournament.tournament_name,
            'location': tournament.location,
            'tour_number': tournament.tour_number,
            'time_controller': tournament.time_controller,
            'number_of_players': tournament.number_of_players,
            'description': tournament.description,
            'players_list': tournament.players_list,
            'round_list': tournament.round_list
        }
        return serialized_tournament

    def deserialize_tournament(self, tournament):
        tournament_name = tournament.tournament_name,
        location = tournament.location,
        tour_number = tournament.tour_number,
        time_controller = tournament.time_controller,
        number_of_players = tournament.number_of_players,
        description = tournament.description,

        tournament_infos = {
            'tournament_name': tournament_name,
            'location': location,
            'tour_number': tour_number,
            'time_controller': time_controller,
            'number_of_players': number_of_players,
            'description': description
        }
        return tournament_infos

        # TODO : add player to tournament
        # players_list = tournament.players_list,

        # TODO : add rounds to tournament
        # round_list = tournament.round_list