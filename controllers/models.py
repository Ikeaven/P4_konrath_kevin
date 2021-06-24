import random
from uuid import uuid1

from typing import List


from .view import ViewsController

from paires.suisse import Suisse

from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


from views.round import RoundView
from views.menu import MenuView
from views.player import PlayerView
from views.score import ScoreView
from views.tournament import TournamentView
from views.utilities import UtilitiesView

from config import SCORE_FOR_NULL, SCORE_FOR_WINNER, DEFAULT_TOUR_NUMBER


class ModelsController:

    def __init__(self) -> None:
        self.view_controller = ViewsController()
        self.menu_view = MenuView()
        self.player_view = PlayerView()
        self.round_view = RoundView()
        self.score = ScoreView()
        self.utilities_view = UtilitiesView()
        self.tournois_view = TournamentView()

        self.players: List = []

    def end_of_round(self, tournament):
        """End a round :
            - set an end time to round
            - update score
            - generate new round

        Args:
            tournament (tournament instance): tournament instance
        """
        try:
            round = tournament.round_list[-1]
            if round.end_round_datetime == 'Round en cours':
                round.stop_round()
                self.round_view.display_stop_time(round)
                self.update_score_round(round)
                self.generate_next_round(round, tournament)
            else:
                self.utilities_view.display_tournament_is_finished()
        except AttributeError:
            self.view_controller.display_error()

    def update_score_round(self, round):
        """Update player's score at the end of a round.

        Keyword arguments:
        round : Round -- instance of Round
        """

        for match in round.matchs:
            # On demande : qui est le vainqueur
            winner = self.score.update_score(match)
            # passer le score en variable de config
            if winner == 0:
                # match null
                match.score_player1 += SCORE_FOR_NULL
                match.score_player2 += SCORE_FOR_NULL
            elif winner == 1:
                # player 1 gagne
                match.score_player1 += SCORE_FOR_WINNER

            elif winner == 2:
                # player 2 gagne
                match.score_player2 += SCORE_FOR_WINNER

    def DEMO_import_auto_tournament(self):
        """Create random info for a tournament
        """
        tournament_infos = {'tournament_name': f"tournament_name {random.randint(0, 1000)}",
                            'location': "Strasbourg",
                            'tour_number': '4',
                            'start_date': (
                                f'''{random.randint(10, 20)}/{random.randint(10, 12)}/'''
                                f'''{random.randint(1990, 2000)}'''
                                ),
                            'time_controller': random.randint(1, 3),
                            'number_of_players': '8',
                            'description': 'Description du tournois',
                            'id': str(uuid1())}
        tournament_infos['end_date'] = tournament_infos['start_date']
        tournament_obj = Tournament()
        tournament_obj.add_tournament(tournament_infos)
        self.add_multiple_players(int(tournament_obj.number_of_players), tournament_obj)

        self.generate_first_round(tournament_obj)

    def DEMO_import_auto_players(self, players_number: int, tournois_obj: object):
        """DEMO : import players auto for a tournament


        Args:
            players_number (int): players number in the tournament
            tournois_obj (tournament instance): tournament instance
        """
        self.players = []
        for num_player in range(int(players_number)):
            player_infos = {
                "last_name": f'Nom {str(num_player+1)}',
                "first_name": f'Prénom {str(num_player+1)}',
                "date_of_birth": f'{random.randint(10, 28)}/{random.randint(10, 12)}/{random.randint(1950, 2021)}',
                "sex": 'M' if random.randint(0, 1) else 'F',
                "ranking": random.randint(300, 2000),
                "id": str(uuid1())}
            player_obj = Player()
            player_obj.add_player(player_infos)
            self.players.append(player_obj)
        self.bind_multiple_players_to_tournament(tournois_obj, self.players)
        self.players = []

    #  ______________________________________________________________________

    def create_multiple_player(self, player_info: dict):
        """Create player instance, add to players list

        Args:
            player_info (dict): player informations from user

        """
        player_obj = Player()
        player_obj.add_player(player_info)
        self.players.append(player_obj)

    def create_new_player(self, player_info):
        """Create a player instance

        Args:
            player_info (dict): player informations from user

        Returns:
            player instance
        """
        player_obj = Player()
        player_obj.add_player(player_info)
        return player_obj

    def ask_player_info(self, num_player: int) -> dict:
        """Input player informations, ask to user

        Args:
            num_player (int): player number to show
                - it can be number in the turnament
                - or count of all players

        Returns:
            dict: player info
        """
        player_info: dict = self.player_view.get_player_info(num_player + 1)
        id = str(uuid1())
        player_info['id'] = str(id)
        return player_info

    def check_players_list(self, tournament_obj):
        """Get a list of players without player already in the tournament

        Args:
            tournament_obj (tournament instance): tournament instance

        Returns:
            List : List of all players, without players already in the tournament
        """
        check_list = list(Player.LIST_PLAYERS)
        for player in tournament_obj.players_list:
            if player in check_list:
                check_list.remove(player)
        return check_list

    def import_players_manuel(self, players_number, tournament_obj):
        """Import player to a tournament
            - already saved player
            - Input new player

        Args:
            players_number (int): player number for this tournament
            tournament_obj (tournament instance): tournament instance where we wants to imports players
        """
        for num_player in range(int(players_number)):
            # check_list is a list of all players without players already binded with tournament
            check_list = self.check_players_list(tournament_obj)
            # Display menu if
            if len(check_list) != 0:
                while True:
                    selected_menu = self.menu_view.display_menu_add_player()
                    # Player already saved
                    if selected_menu == '1':
                        self.player_view.display_players_list(check_list)
                        player_id = int(self.menu_view.select_item('joueur'))
                        try:
                            player = check_list[player_id]
                        except IndexError:
                            self.utilities_view.display_error_with_message('Index non trouvé !!')
                        if player in tournament_obj.players_list:
                            self.utilities_view.display_error_with_message('Joueur déjà enregistré dans ce tournoi !!')
                        else:
                            self.bind_player_to_tournament(tournament_obj, player)
                            break
                    # input new player
                    elif selected_menu == '2':
                        player_info = self.ask_player_info(num_player)
                        player = self.create_new_player(player_info)
                        self.bind_player_to_tournament(tournament_obj, player)
                        break
                    else:
                        self.utilities_view.display_error()
            # input new player
            else:
                player_info = self.ask_player_info(num_player)
                player = self.create_new_player(player_info)
                self.bind_player_to_tournament(tournament_obj, player)

    def add_multiple_players(self, players_number: int, tournament_obj: object):
        """Add players to a tournament.

        Keyword arguments:
        players_number : int -- number of players to add
        """
        selected_menu = self.menu_view.import_auto_or_manuel_menu()
        self.player_import_type(selected_menu, players_number, tournament_obj)

    def player_import_type(self, selected_menu, players_number, tournois_obj):
        """Select a way to import players :
                - auto
                - manuel

        Args:
            selected_menu (int): selection by user
            players_number (int): number for a player
            tournois_obj (tournament instance): instance du tournoi.
        """
        # import auto
        if selected_menu == '1':
            self.DEMO_import_auto_players(players_number, tournois_obj)
        # import manuel
        elif selected_menu == '2':
            self.import_players_manuel(players_number, tournois_obj)
        else:
            self.view_controller.display_error()

    def bind_player_to_tournament(self, tournament_obj, player_obj):
        """Bind player to a tournament :
            Add player instance to a list in the tournament instance.

        Args:
            tournament_obj (Tournament instance): tournament where we want to link players
            player_obj (Player instance): player we want to link
        """
        tournament_obj.bind_player(player_obj)

    def bind_multiple_players_to_tournament(self, tournament_obj: object, players: List[Player]):
        """Add players lists to tournament.

        Keyword arguments:
        tournois_obj : Tournament -- Instance of Tournament
        players : [Player] -- List of Player's instance
        """
        tournament_obj.bind_multiple_players(players)

    def generate_first_round(self, tournois_obj):
        """Create first round.

        Keyword arguments:
        tournois_obj : Tournament -- Instance de class Tournament
        """
        # generate_first_round renvoi une liste de tuple
        # => pair de joueur [(player1, player2), (player1, player2), ...]
        first_round_list = Suisse().generate_first_round(tournois_obj.players_list)
        self.round = Round().create_round('Round 1')
        for players in first_round_list:
            # Create match instance - init score
            match = Match().create_match(players[0], 0, players[1], 0)
            self.round.add_match_to_round(match)
        #  Création du match suivant, et affichage des prochains matchs
        tournois_obj.add_round(self.round)
        RoundView().start_new_round(self.round)
        self.view_controller.display_match_of_round(self.round)

    def generate_next_round(self, previous_round, tournois_obj):
        """Create the next round.

        Keyword arguments:
        previous_round : Round -- round instance that has just ended
        tournois_obj : Tournament -- Instance of Tournament
        """
        # Check tour number
        if len(tournois_obj.round_list) < DEFAULT_TOUR_NUMBER:

            match_list = Suisse().generate_next_round(previous_round, tournois_obj)

            self.round = Round().create_round(f'Round {len(tournois_obj.round_list)+1}')
            RoundView().start_new_round(self.round)
            for match in match_list:
                formated_match = Match().create_match(match[0][0], match[0][1], match[1][0], match[1][1])
                self.round.add_match_to_round(formated_match)
            tournois_obj.add_round(self.round)
            self.view_controller.display_match_of_round(self.round)

        # end of tournament => display final score
        else:
            # récupérer la liste triée:
            players = Suisse().get_players_list_with_score(tournois_obj.round_list[-1])
            sorted_list = Suisse().sort_list_by_score(players)
            self.score.display_final_score(sorted_list)
            print("Fin du tournois")

    # Create Tournament
    def create_tournament(self):
        """Create tournament instance with user informations."""
        tournament_infos = self.tournois_view.get_tournament_info()
        tournament_infos['id'] = str(uuid1())
        tournois_obj = Tournament()
        tournois_obj.add_tournament(tournament_infos)

        self.add_multiple_players(int(tournois_obj.number_of_players), tournois_obj)

        self.generate_first_round(tournois_obj)
