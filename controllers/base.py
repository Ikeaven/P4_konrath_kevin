#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Base Controller."""

# TODO Enlever les appele de classes sauvages. ex : Tournament()... si ça change faudra le chercher dans tout le code...

# import time
import random
# import sys

from config import DEFAULT_TOUR_NUMBER, SCORE_FOR_WINNER, SCORE_FOR_NULL

from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from views.utilities import UtilitiesView

from views.score import ScoreView
from views.round import RoundView

from serializers.player import PlayerSerializer
from serializers.tournament import TournamentSerializer
from db.tinydb import insert_players_to_db, insert_tournaments_to_db

# from utilities.checker import checker_text_field, checker_menu, checker_digit_field
# from utilities.checker import checker_digit_or_empy_default_field

from paires.suisse import Suisse


class Controller:
    """Main Controller."""

    def __init__(self, menu_view, player_view, tournament_view):
        """Init Controller.

        Args:
            menu_view (View): Display menus
            player_view (View): Display players view
            tournament_view (View): Display tournament view
        """
        # models
        self.players: List[Player] = []
        self.tournaments: List[Tournament] = []

        # views
        self.menu_view = menu_view
        self.player_view = player_view
        self.tournament_view = tournament_view
        self.utilities_view = UtilitiesView()
        self.score = ScoreView()

        self.running = True

    def routing_main_menu(self, selected_menu):
        """Cette fonction déclenche des méthodes en fonction du choix de l'utilisateur."""
        # Créer un nouvau tournoi
        if selected_menu == '1':

            self.create_tournament()

        # Éditer un tournoi
        elif selected_menu == '2':
            # TODO : choisir le tournois à éditer
            # TODO :remplir les champs
            self.edit_tournament()

        # Editer joueur
        elif selected_menu == '3':
            # TODO Choisir le joueur et modifier
            self.player_view.display_players_list(self.players)

        # Rapports
        elif selected_menu == '4':
            self.routing_menu_reports()

        # Afficher les tournois
        elif selected_menu == '5':
            self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)

        # fin de round
        elif selected_menu == '6':
            # TODO : créer une méthode pour ça
            try:
                self.round.stop_round()
                round_view = RoundView()
                round_view.display_stop_time(self.round)
                self.update_score_round(self.round)

                self.generate_next_round(self.round, self.tournois_obj)
            except AttributeError:
                self.utilities_view.display_error()

        # Sauvegarder
        elif selected_menu == '7':
            self.save_to_tinydb(Player().LIST_PLAYERS, Tournament().LISTE_TOURNOIS)

        # TEST générer tournois auto
        elif selected_menu == '8':
            self.TEST_import_auto_tournoi()

        # stop
        elif selected_menu == '9':
            self.running = False

        # Choix n'est pas dans les propositions du menu
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

    def save_to_tinydb(self, players, tournaments):
        """Save players and tournaments into json file."""
        serialized_player = []
        for player in players:
            serialized_player.append(PlayerSerializer().serialize_player(player))
        insert_players_to_db(serialized_player)

        serialized_tournament = []
        for tournament in tournaments:
            serialized_tournament.append(TournamentSerializer().serialize_tournament(tournament))
        insert_tournaments_to_db(serialized_tournament)

    def display_match_of_tournament(self):
        """Select the tournament and Call the view to display match of a tournament."""
        # TODO : function select item... 
        selected_tournament = self.select_tournament()
        RoundView().display_round(selected_tournament, True)

    def display_round_of_tournament(self):
        """Call the view to display round of tournament."""
        # TODO : fucntion select item
        selected_tournament = self.select_tournament()
        RoundView().display_round(selected_tournament)

    def select_tournament(self):
        """Allow the user to choose the turnament.

        Returns:
            instance of Tournament
        """
        # Selectionner un tournoi -> afficher les tournois
        self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)
        # choisir l'ordre d'affichage
        number_item = self.menu_view.select_item()
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

    def rooting_sort_by(self, players):
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

    def display_players_of_tournament(self):
        """Display players of a tournament."""
        # affiche les tournois - et choix
        selected_tournament = self.select_tournament()
        # afficher les joueurs du tournoi
        players = selected_tournament.players_list
        # Ranger la liste par ordre alphabetique ou par classement
        sorted_list = self.rooting_sort_by(players)
        # afficher les joueurs par ordre souhaité
        self.player_view.display_players_list(sorted_list)

    def get_all_players_from_model(self):
        """Display all players."""
        self.all_players = Player().get_all_players()
        self.player_view.display_players_list(self.all_players)

    def edit_tournament(self):
        """Allow users to edit a tournament."""
        #  TODO : fonction choose your item
        self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)
        item_index = self.menu_view.select_item()
        tournoi = Tournament().LISTE_TOURNOIS[int(item_index)]
        print(tournoi.tournament_name)
        # TODO : EDIT a proprement parler... 

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
    # TODO : A SUPPRIMER pour la mise en production
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
                            'description': 'Description du tournois'}
        self.tournois_obj = Tournament()
        self.tournois_obj.add_tournament(tournament_infos)
        self.tournaments.append(self.tournois_obj)
        self.add_multiple_players(self.tournois_obj.number_of_players)

        self.generate_first_round(self.tournois_obj)

    # AUTO REMPLISSAGE POUR TESTER PLUS FACILEMENT
    # TODO : A SUPPRIMER
    def TEST_import_auto_players(self, players_number):
        """Cette méthode génère automatiquement des instance de Player
        avec attributs aléatoires

        Keyword arguments:
        players_number : int -- Nombre de joueurs à créer
        """
        for num_player in range(int(players_number)):
            player_infos = {
                "last_name": f'Nom {str(num_player+1)}',
                "first_name": f'Prénom {str(num_player+1)}',
                "date_of_birth": f'{random.randint(10, 28)}/{random.randint(10, 12)}/{random.randint(1950, 2021)}',
                "sex": 'M' if random.randint(0, 1) else 'F',
                "ranking": random.randint(300, 2000)}
            player_obj = Player()
            player_obj.add_player(player_infos)
            self.players.append(player_obj)
            self.bind_player_to_tournament(self.tournois_obj, self.players)
            self.players = []

    def add_multiple_players(self, players_number):
        """Add players to a tournament.

        Keyword arguments:
        players_number : int -- number of players to add 
        """

        # TODO : REMPLISSAGE AUTO A SUPPRIMER => POUR TEST
        # MENU À SUPPRIMER POUR LA PRODUCTION
        menu = self.menu_view.test_import_auto()
        if menu == '1':
            self.TEST_import_auto_players(players_number)
        elif menu == '2':
            for num_player in range(int(players_number)):
                selected_menu = self.menu_view.display_menu_add_player()
                #  Ajouter un joueur déjà enregistré
                if selected_menu == '1':
                    self.get_all_players_from_model()
                    # TODO : selectionner le joueur à ajouter
                # Saisir un nouveau joueu
                elif selected_menu == '2':
                    player_info = self.player_view.get_player_info(num_player + 1)
                    player_obj = Player()
                    player_obj.add_player(player_info)
                    self.players.append(player_obj)
                else:
                    self.utilities_view.display_error()
        # A SUPPRIMER - fait parti du menu IMPORT AUTO
        else:
            self.utilities_view.display_error()

    def bind_player_to_tournament(self, tournament_obj, players):
        """Add players lists to tournament.

        Keyword arguments:
        tournois_obj : Tournament -- Instance of Tournament
        players : [Player] -- List of Player's instance
        """
        tournament_obj.bind_players(players)

    def display_match_of_round(self, round):
        """Display all matchs of a round

        Keyword arguments:
        round : Round -- Instance of Round
        """
        for match in round.matchs:
            self.score.display_match(match)

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
            print("Fin du tournois => scores")

    def create_tournament(self):
        """Create Tournament.

        We will ask the user to fill in the tournament information.
        """

        # Saisi des informations du tournoi
        tournament_infos = self.tournament_view.get_tournament_info()

        self.tournois_obj = Tournament()
        self.tournois_obj.add_tournament(tournament_infos)

        # TODO : a remplacer par la liste du modèle
        self.tournaments.append(self.tournois_obj)

        # number_of_player = self.get_players_number()
        self.add_multiple_players(self.tournois_obj.number_of_players)

        self.bind_player_to_tournament(self.tournois_obj, self.players)
        # remis à zéro pour le prochain tournoi
        self.players = []

        self.generate_first_round(self.tournois_obj)

    def main_menu(self):
        """Diplay main menu."""
        selected_menu = self.menu_view.display_menu()
        self.routing_main_menu(selected_menu)

    def run(self):
        """App loop."""
        while self.running:
            self.main_menu()
