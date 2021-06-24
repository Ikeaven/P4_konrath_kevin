""" DataBase Controller """


from controllers.models import ModelsController

from serializers.player import PlayerSerializer
from serializers.tournament import TournamentSerializer
from serializers.round import RoundSerializer
from serializers.match import MatchSerializer

from models.tournament import Tournament
from models.player import Player
from models.match import Match
from models.round import Round

from db.tinydb import Database


class DBController:
    # Save

    def __init__(self) -> None:
        self.database = Database()
        self.models_controller = ModelsController()

    def save_players(self, players):
        """Save the players in the database.
            - serialize players
            - insert to database.

        Args:
            players (List): List of player instance
        """
        serialized_player = []
        for player in players:
            serialized_player.append(PlayerSerializer().serialize_player(player))
        self.database.insert_players_to_db(serialized_player)

    def save_tournaments(self, tournaments):
        """Save the tournaments in the database:
            - serialize tournament
            - insert to database

        Args:
            tournaments (Tournament instance): tournament instance to save
        """
        serialized_tournaments = []
        for tournament in tournaments:
            serialized_tournaments.append(TournamentSerializer().serialize_tournament(tournament))
            serialized_rounds = []
            for round in tournament.round_list:
                serialized_rounds.append(RoundSerializer().serialize_round(round))
                serialized_matchs = []
                for match in round.matchs:
                    serialized_matchs.append(MatchSerializer().serialize_matchs(match))

                self.database.insert_matchs_to_db(serialized_matchs)
            self.database.insert_rounds_to_db(serialized_rounds)
        self.database.insert_tournaments_to_db(serialized_tournaments)

    def save_to_tinydb(self, players, tournaments):
        """Save players and tournaments in database."""
        self.database.clear_db()
        self.save_players(players)
        self.save_tournaments(tournaments)

    # Loads
    def load_tournaments(self):
        """Load tournament from database
            - Get tournaments info from database
            - Create tournaments instances.
        """
        tournaments: list[dict] = self.database.get_all_tournaments()
        for tournament in tournaments:
            # We only create a new instance if we don't already have it
            if tournament['id'] not in (tournament.id for tournament in Tournament.TOURNAMENT_LIST):
                # create tournament object with attributs
                tournament_obj = Tournament()
                tournament_dict = {
                            'id': tournament['id'],
                            'tournament_name': tournament['tournament_name'],
                            'location': tournament['location'],
                            'start_date': tournament['start_date'],
                            'end_date': tournament['end_date'],
                            'tour_number': tournament['tour_number'],
                            'time_controller': tournament['time_controller'],
                            'number_of_players': tournament['number_of_players'],
                            'description': tournament['description']}
                tournament_obj.add_tournament(tournament_dict)
                # load round for this tournament
                self.load_rounds(tournament_obj)
                # bind player with this tournament
                tournament_player = []
                for player_id in tournament['players_list']:
                    tournament_player.append(Player.get_player_by_id(player_id))
                tournament_obj.bind_multiple_players(tournament_player)
            else:
                pass

    def load_players(self):
        """Load players from database
            - Get players info from database
            - Create players instances.
        """
        players: list = self.database.get_all_players()
        for player in players:
            # We only create new instance if we don't already have it
            if player['id'] not in (player.id for player in Player.LIST_PLAYERS):
                player_dict = {
                    "id": player['id'],
                    "last_name": player['last_name'],
                    "first_name": player['first_name'],
                    "date_of_birth": player['date_of_birth'],
                    "sex": player['sex'],
                    "ranking": player['ranking']
                }
                self.models_controller.create_multiple_player(player_dict)
            else:
                pass

    def load_rounds(self, tournament):
        """Load rounds for a tournament from database

        Args:
            tournament (tournament instance): specify a tournament to get his rounds
        """
        rounds: list[dict] = self.database.get_all_rounds_of_tournament(tournament.id)
        for round in rounds:
            round_dict = {
                "id": round['id'],
                "round_name": round['round_name'],
                "start_round_datetime": round['start_round_datetime'],
                "end_round_datetime": round['end_round_datetime']
            }
            round_obj = Round().load_round(round_dict)
            # import pdb; pdb.set_trace()
            tournament.add_round(round_obj)
            self.load_matchs(round)

    def load_matchs(self, round: dict):
        """Load matchs for a round from database

        Args:
            round (dict): round infos
        """
        matchs: list[dict] = self.database.get_all_matchs_of_round(round['id'])
        for match in matchs:
            match_dict = {
                "id": match["id"],
                "player1": Player.get_player_by_id(match['player1']),
                "score_player1": match['score_player1'],
                "player2": Player.get_player_by_id(match['player2']),
                "score_player2": match['score_player1']
            }
            match: object = Match().load_match(match_dict)
            round_obj: object = Round.find_round_by_id(round['id'])
            round_obj.add_match_to_round(match)
