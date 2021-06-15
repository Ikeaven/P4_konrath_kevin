#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Base Controller."""

# TODO Enlever les appele de classes sauvages. ex : Tournament()... si ça change faudra le chercher dans tout le code...

# import time
import pdb
import random
import uuid
# import sys

from config import DEFAULT_TOUR_NUMBER, SCORE_FOR_WINNER, SCORE_FOR_NULL

from typing import List
from models import tournament

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from views.utilities import UtilitiesView

from views.score import ScoreView
from views.round import RoundView

from db.tinydb import Database

from serializers.player import PlayerSerializer
from serializers.tournament import TournamentSerializer
from serializers.round import RoundSerializer
from serializers.match import MatchSerializer

# from utilities.checker import checker_text_field, checker_menu, checker_digit_field
# from utilities.checker import checker_digit_or_empy_default_field

from paires.suisse import Suisse


class Controller:
    """Main Controller."""

    # init
    def __init__(self, menu_view, player_view, tournament_view):
        """Init Controller.

        Args:
            menu_view (View): Display menus
            player_view (View): Display players view
            tournament_view (View): Display tournament view
        """
        # models 
        # TODO : normanelent je n'ai pas besoin de ces listes la... 
        self.players: List[Player] = []
        self.tournaments: List[Tournament] = []

        # views
        self.menu_view = menu_view
        self.player_view = player_view
        self.tournament_view = tournament_view
        self.utilities_view = UtilitiesView()
        self.score = ScoreView()

        self.database = Database()

        self.running = True

    # Rounting
    def routing_main_menu(self, selected_menu):
        """Cette fonction déclenche des méthodes en fonction du choix de l'utilisateur."""
        # Create new tournament
        if selected_menu == '1':

            self.create_tournament()

        # Edit tournament
        elif selected_menu == '2':
            selected_tournament = self.select_tournament()
            self.routing_edit_tournament(selected_tournament)

        # Edit player
        elif selected_menu == '3':
            # TODO Choisir le joueur et modifier
            self.player_view.display_players_list(Player.get_all_players())
            player_id : int = int(self.menu_view.select_item('joueur'))
            selected_player : object = Player.get_all_players()[player_id]
            self.routing_edit_player(selected_player)

        # Rapports
        elif selected_menu == '4':
            self.routing_menu_reports()

        # Load data from database
        elif selected_menu == '5':
            self.load_players()
            self.load_tournaments()
            
            
        # end of round
        # elif selected_menu == '6':
        #     # TODO Passer ce menu dans editer un tournoi
        #     try:
        #         self.round.stop_round()
        #         round_view = RoundView()
        #         round_view.display_stop_time(self.round)
        #         self.update_score_round(self.round)
        #         # FIXME : LIGNE EN DESSOUS A fixer => tournois_obj not defined
        #         # self.generate_next_round(self.round, tournois_obj)
        #     except AttributeError:
        #         self.utilities_view.display_error()

        # Save
        elif selected_menu == '7':
            self.save_to_tinydb(Player().LIST_PLAYERS, Tournament().LISTE_TOURNOIS)

        # TEST generate tournament auto
        elif selected_menu == '8':
            self.TEST_import_auto_tournoi()

        # stop
        elif selected_menu == '9':
            self.running = False

        # error : value not found
        else:
            self.utilities_view.display_error()

    def routing_edit_tournament(self, tournament:object):
        selected_menu = self.menu_view.display_menu_edit_tournament(tournament)
        # end of the round -> update score
        if selected_menu == '1':
            self.end_of_round(tournament)
        # change name of tournament
        elif selected_menu == '2':
            new_tournament_name = self.tournament_view.update_tournament_name(tournament)
            tournament.update_name(new_tournament_name)
        # change description
        elif selected_menu == '3':
            new_description = self.tournament_view.update_tournament_description(tournament)
            tournament.update_description(new_description)
        # change time controller
        elif selected_menu == '4':
            new_time_controller = self.tournament_view.update_time_controller(tournament)
            tournament.update_time_controller(new_time_controller)
        # return to main menu
        elif selected_menu == '5':
            self.main_menu()
        # error : value not found
        else:
            self.utilities_view.display_error()

    def routing_edit_player(self, player:object):
        selected_menu = self.menu_view.display_menu_edit_player()
        # Editer the ranking
        if selected_menu == '1':
            new_ranking = self.player_view.update_ranking(player)
            player.update_ranking(new_ranking)

        # Edit first name and last name
        elif selected_menu == '2':
            new_first_name, new_last_name = self.player_view.update_name(player)
            player.update_name(new_first_name, new_last_name)
        # Edit date of birth
        elif selected_menu == '3':
            new_date_of_birth = self.player_view.update_birthday(player)
            player.update_birthday(new_date_of_birth)
        #  Edit sex
        elif selected_menu == '4':
            new_sex = self.player_view.update_sex(player)
            player.update_sex(new_sex)
        # Return to main menu
        elif selected_menu == '5':
            pass
        else:
            self.utilities_view.display_error()
            
    def routing_menu_reports(self):
        """Choice - Menu reports."""
        selected_menu = self.menu_view.display_report_menu()

        # Afficher tous les joueurs
        if selected_menu == '1':
            # TODO demande dans quel tri -> Alpha / Classement
            players = Player.LIST_PLAYERS
            self.player_view.display_players_list(players)

        # Afficher les joueurs d'un tournois
        elif selected_menu == '2':
            self.display_players_of_tournament()

        # Afficher les tournois
        elif selected_menu == '3':
            self.tournament_view.display_tournament_list(Tournament.LISTE_TOURNOIS)

        # Afficher les rounds d'un tournoi
        elif selected_menu == '4':
            self.display_round_of_tournament()

        # Liste des matchs d'un tournoi
        elif selected_menu == '5':
            self.display_match_of_tournament()

        # retour au menu principal
        elif selected_menu == '6':
            self.main_menu()

        # Le choix n'est pas dans les propositions du menu
        else:
            UtilitiesView().display_error()

    def routing_sort_by(self, players):
            # TODO : à simplifier ... 
            
            """Cette fonction va renvoyer une liste de joueurs, ranger dans l'ordre en fonction de notre choix.

            - ordre alphabetique
            - ordre par classement

            Keyword arguments:
            players : [array] -- liste d'instance de Player
            Return [array]: sorted_list -- la liste de joueurs ordonné
            """
            sort_by = self.menu_view.select_sorting()
            # tri alphabetique
            if sort_by == '1':
                sorted_list = self.sort_list_by(players, "last_name")
                return sorted_list

            # tri par classement
            elif sort_by == '2':
                sorted_list = self.sort_list_by(players, "ranking")
                return sorted_list

            # bad request
            else:
                UtilitiesView().display_error()

    # Save 
    def save_to_tinydb(self, players, tournaments):
        """Save players and tournaments into json file."""
        self.database.clear_db()
        serialized_player = []
        for player in players:
            serialized_player.append(PlayerSerializer().serialize_player(player))
        self.database.insert_players_to_db(serialized_player)

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

    # Loads
    def load_tournaments(self):
        tournaments : list[dict]= self.database.get_all_tournaments()
        for tournament in tournaments:
            # We only create a new instance if we don't already have it
            if tournament['id'] not in (tournament.id for tournament in Tournament.LISTE_TOURNOIS):
                # create tournament object with attributs  
                tournament_obj = Tournament()
                tournament_dict = {
                            'id': tournament['id'],
                            'tournament_name': tournament['tournament_name'],
                            'location': tournament['location'],
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
                tournament_obj.bind_players(tournament_player)
            else:
                pass

    def load_players(self):
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
                self.create_player(player_dict)
                
            else:
                pass
        

    def load_rounds(self, tournament):
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
        matchs : list[dict] = self.database.get_all_matchs_of_round(round['id'])
        for match in matchs:
            match_dict = {
                "id": match["id"],
                "player1": Player.get_player_by_id(match['player1']),
                "score_player1": match['score_player1'],
                "player2": Player.get_player_by_id(match['player2']),
                "score_player2": match['score_player1']
            }
            match : object = Match().load_match(match_dict)
            round_obj : object = Round.find_round_by_id(round['id'])
            round_obj.add_match_to_round(match)

    # Display lists 
    def display_match_of_tournament(self):
        """Select the tournament and call the view to display match of a tournament."""
        # TODO : function select item... 
        selected_tournament = self.select_tournament()
        RoundView().display_round(selected_tournament, True)

    def display_round_of_tournament(self):
        """Call the view to display round of tournament."""
        # TODO : fucntion select item
        selected_tournament = self.select_tournament()
        RoundView().display_round(selected_tournament)

    def select_tournament(self) -> object:
        """Allow the user to choose the turnament.

        Returns:
            instance of Tournament
        """
        # Selectionner un tournoi -> afficher les tournois
        self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)
        # choisir l'ordre d'affichage
        number_item = self.menu_view.select_item('tournois')
        selected_tournament = Tournament().LISTE_TOURNOIS[int(number_item)]
        return selected_tournament

    def sort_list_by(self, players, tri):
        """Sort the list of players by ranking or alphabetical order.

        Args:
            players ([Players list]): List of players instances
            tri (str): must be 'ranking' or 'last_name'

        Returns:
            [Players list]: sorted list of players instances
        """
        if tri == 'ranking':
            sorted_list = sorted(players, key = lambda x: x.ranking, reverse=True)
        elif tri == 'last_name':
            sorted_list = sorted(players, key = lambda x: x.last_name, reverse=False)
        return sorted_list
    
    def display_players_of_tournament(self):
        """Display players of a tournament."""
        # affiche les tournois - et choix
        selected_tournament = self.select_tournament()
        # afficher les joueurs du tournoi
        players = selected_tournament.players_list
        # Ranger la liste par ordre alphabetique ou par classement
        sorted_list = self.routing_sort_by(players)
        # afficher les joueurs par ordre souhaité
        self.player_view.display_players_list(sorted_list)

    def get_all_players_from_model(self):
        """Display all players."""
        self.all_players = Player.get_all_players()
        self.player_view.display_players_list(self.all_players)

    def display_match_of_round(self, round):
        """Display all matchs of a round

        Keyword arguments:
        round : Round -- Instance of Round
        """
        for match in round.matchs:
            self.score.display_match(match)    

    # ADD & Updates 
    
    def end_of_round(self, tournament):
        try:
            round = tournament.round_list[-1]
            if round.end_round_datetime == 'Round en cours':
                round.stop_round()
                round_view = RoundView()
                round_view.display_stop_time(round)
                self.update_score_round(round)
                self.generate_next_round(round, tournament)
            else:
                self.utilities_view.display_tournament_is_finished()
        except AttributeError:
            self.utilities_view.display_error()

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

    # AUTO REMPLISSAGE POUR TESTER PLUS FACILEMENT
    #  ______________________________________________________________________
    # TODO : A SUPPRIMER pour la mise en production ⬇️
    def TEST_import_auto_tournoi(self):
        """ Cette méthode génère une instance de tournoi
        avec des attributs aléatoires.

        A SUPPRIMER POUR LA PRODUCTION
        """
        tournament_infos = {'tournament_name': f"tournament_name {random.randint(0, 1000)}",
                            'location': "Strasbourg",
                            'tour_number': '4',
                            'time_controller': f'{random.randint(1,3)}',
                            'number_of_players': '8',
                            'description': 'Description du tournois', 
                            'id': str(uuid.uuid1())}
        tournament_obj = Tournament()
        tournament_obj.add_tournament(tournament_infos)
        # self.tournaments.append(tournois_obj)
        self.add_multiple_players(int(tournament_obj.number_of_players), tournament_obj)

        self.generate_first_round(tournament_obj)

    # AUTO REMPLISSAGE POUR TESTER PLUS FACILEMENT
    # TODO : A SUPPRIMER ⬇️
    def TEST_import_auto_players(self, players_number:int, tournois_obj:object):
        """Cette méthode génère automatiquement des instance de Player
        avec attributs aléatoires

        Keyword arguments:
        players_number : int -- Nombre de joueurs à créer
        """
        self.players = []
        for num_player in range(int(players_number)):
            player_infos = {
                "last_name": f'Nom {str(num_player+1)}',
                "first_name": f'Prénom {str(num_player+1)}',
                "date_of_birth": f'{random.randint(10, 28)}/{random.randint(10, 12)}/{random.randint(1950, 2021)}',
                "sex": 'M' if random.randint(0, 1) else 'F',
                "ranking": random.randint(300, 2000),
                "id": str(uuid.uuid1())}
            player_obj = Player()
            player_obj.add_player(player_infos)
            self.players.append(player_obj)
            self.bind_player_to_tournament(tournois_obj, self.players)
            self.players = []
            
    #  ______________________________________________________________________

    def create_player(self, player_info: dict):
        player_obj = Player()
        player_obj.add_player(player_info)
        # self.players.append(player_obj)

    def add_multiple_players(self, players_number:int, tournament_obj:object):
        """Add players to a tournament.

        Keyword arguments:
        players_number : int -- number of players to add 
        """

        # TODO : REMPLISSAGE AUTO A SUPPRIMER => POUR TEST
        # MENU À SUPPRIMER POUR LA PRODUCTION
        menu = self.menu_view.test_import_auto()
        if menu == '1':
            self.TEST_import_auto_players(players_number, tournament_obj)
        elif menu == '2':
            for num_player in range(int(players_number)):
                selected_menu = self.menu_view.display_menu_add_player()
                #  Ajouter un joueur déjà enregistré
                if selected_menu == '1':
                    self.get_all_players_from_model()
                    # TODO : selectionner le joueur à ajouter
                # Saisir un nouveau joueu
                elif selected_menu == '2':
                    player_info : dict = self.player_view.get_player_info(num_player + 1)
                    id = str(uuid.uuid1())
                    player_info['id'] = str(id)
                    
                    self.create_player(player_info)
                    
                else:
                    self.utilities_view.display_error()
        # A SUPPRIMER - fait parti du menu IMPORT AUTO
        else:
            self.utilities_view.display_error()

    def bind_player_to_tournament(self, tournament_obj:object, players:object):
        """Add players lists to tournament.

        Keyword arguments:
        tournois_obj : Tournament -- Instance of Tournament
        players : [Player] -- List of Player's instance
        """
        tournament_obj.bind_players(players)

    # Create rounds
    def generate_first_round(self, tournois_obj):
        """Create first round.

        Keyword arguments:
        tournois_obj : Tournament -- Instance de class Tournament
        """
        # generate_first_round renvoi une liste de tuple => pair de joueur [(player1, player2), (player1, player2), ...]
        first_round_list = Suisse().generate_first_round(tournois_obj.players_list)
        self.round = Round().create_round('Round 1')
        for players in first_round_list:
            # création de l'instance de match - initialisation du score
            match = Match().create_match(players[0], 0, players[1], 0)
            self.round.add_match_to_round(match)
        #  Création du match suivant, et affichage des prochains matchs
        tournois_obj.add_round(self.round)
        RoundView().start_new_round(self.round)
        self.display_match_of_round(self.round)

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
            self.display_match_of_round(self.round)

        # end of tournament => display final score
        else:
            # récupérer la liste triée:
            players = Suisse().get_players_list_with_score(tournois_obj.round_list[-1])
            sorted_list = Suisse().sort_list_by_score(players)
            self.score.display_final_score(sorted_list)
            print("Fin du tournois")

    # Create Tournament
    def create_tournament(self):
        """Create Tournament.

        We will ask the user to fill in the tournament information.
        """

        # Saisi des informations du tournoi
        tournament_infos = self.tournament_view.get_tournament_info()
        tournament_infos['id'] = str(uuid.uuid1())
        tournois_obj = Tournament()
        tournois_obj.add_tournament(tournament_infos)

        # TODO : a remplacer par la liste du modèle
        self.tournaments.append(tournois_obj)

        # number_of_player = self.get_players_number()
        self.add_multiple_players(int(tournois_obj.number_of_players), tournois_obj)

        self.bind_player_to_tournament(tournois_obj, self.players)
        # remis à zéro pour le prochain tournoi
        self.players = []

        self.generate_first_round(tournois_obj)

    # main
    def main_menu(self):
        """Diplay main menu."""
        selected_menu = self.menu_view.display_menu()
        self.routing_main_menu(selected_menu)

    def run(self):
        """App loop."""
        while self.running:

            self.main_menu()
