#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO : Module summary
"""

# import time
import random
# import sys

from config import DEFAULT_TOUR_NUMBER

from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from views.utilities import UtilitiesView

from views.score import ScoreView
from views.round import RoundView

# from utilities.checker import checker_text_field, checker_menu, checker_digit_field
# from utilities.checker import checker_digit_or_empy_default_field

from paires.suisse import Suisse


class Controller:
    """Main Controller."""

    def __init__(self, menu_view, player_view, tournament_view):
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

    def routing_menu_principal(self, selected_menu):
        if selected_menu == '1':
            # Créer un nouvau tournoi
            self.create_tournament()

        elif selected_menu == '2':
            # Éditer un tournoi
            # afficher les tournois
            # choisir le tournois à éditer
            # remplir les champs
            self.edit_tournament()

        elif selected_menu == '3':
            # Editer joueur
            self.player_view.display_players_list(self.players)

        elif selected_menu == '4':
            # Rapports
            self.routing_menu_reports()

        elif selected_menu == '5':
            # Afficher les tournois
            self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)

        elif selected_menu == '6':
            # fin de round
            try:
                self.round.stop_round()
                round_view = RoundView()
                round_view.display_stop_time(self.round)
                self.update_score_round(self.round)

                self.generate_next_round(self.round, self.tournois_obj)
            except AttributeError:
                self.utilities_view.display_error()

        elif selected_menu == '8':
            # TEST générer tournois auto
            self.TEST_import_auto_tournoi()

        elif selected_menu == '9':
            # stop
            self.running = False
        else:
            # Choix n'est pas dans les propositions du menu
            self.utilities_view.display_error()

    def routing_menu_reports(self):
        selected_menu = self.menu_view.display_report_menu()
        if selected_menu == '1':
            # TODO demande dans quel tri -> Alpha / Classement
            players = Player.LIST_PLAYERS
            self.player_view.display_players_list(players)
        elif selected_menu == '2':
            # liste des joueurs d'un tournois
            # Selectionner un tournoi -> afficher les tournois
            self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)
            # choisir l'ordre d'affichage
            selected_item = self.menu_view.select_item()
            # afficher les joueurs du tournoi
            players = Tournament().LISTE_TOURNOIS[int(selected_item)].players_list
            # TODO demander dans quel tri il faut afficher
            self.player_view.display_players_list(players)


        elif selected_menu == '3':
            # Liste des tournois
            pass
        elif selected_menu == '4':
            # Liste des tours d'un tournoi
            pass
        elif selected_menu == '5':
            # Liste des matchs d'un tournoi
            pass
        elif selected_menu == '6':
            # retour au menu principal
            self.menu_principal()
        else:
            UtilitiesView().display_error()

    def get_all_players_from_model(self):
        self.all_players = Player().get_all_players()
        self.player_view.display_players_list(self.all_players)

    def edit_tournament(self):
        self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)
        item_index = self.menu_view.select_item()
        tournoi = Tournament().LISTE_TOURNOIS[int(item_index)]
        print(tournoi.tournament_name)

    def update_score_round(self, round):
        for match in round.matchs:
            winner = self.score.update_score(match)
            if winner == 0:
                # match null
                match.score_player1 += 0.5
                match.score_player2 += 0.5
            elif winner == 1:
                # player 1 gagne
                match.score_player1 += 1

            elif winner == 2:
                # player 2 gagne
                match.score_player2 += 1

    # AUTO REMPLISSAGE POUR TESTER PLUS FACILEMENT
    # TODO : A SUPPRIMER
    def TEST_import_auto_tournoi(self):
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
        ranking = 2000
        for num_player in range(int(players_number)):
            player_infos = {
                "last_name": f'Nom {str(num_player+1)}',
                "first_name": f'Prénom {str(num_player+1)}',
                "date_of_birth": f'{random.randint(10, 28)}/{random.randint(10, 12)}/{random.randint(1950, 2021)}',
                "sex": 'M' if random.randint(0, 1) else 'F',
                "ranking": ranking}
            ranking -= 100
            player_obj = Player()
            player_obj.add_player(player_infos)
            self.players.append(player_obj)
            self.bind_player_to_tournament(self.tournois_obj, self.players)
            self.players = []

    def add_multiple_players(self, players_number):
        # TODO REMPLISSAGE AUTO A SUPPRIMER => POUR TEST
        menu = self.menu_view.test_import_auto()
        if menu == '1':
            self.TEST_import_auto_players(players_number)
        elif menu == '2':
            for num_player in range(int(players_number)):
                selected_menu = self.menu_view.display_menu_add_player()
                if selected_menu == '1':
                    self.get_all_players_from_model()
                    # selectionner le joueur à ajouter
                elif selected_menu == '2':
                    player_info = self.player_view.get_player_info(num_player + 1)
                    player_obj = Player()
                    player_obj.add_player(player_info)
                    self.players.append(player_obj)
                else:
                    self.utilities_view.display_error()
        else:
            self.utilities_view.display_error()

    def bind_player_to_tournament(self, tournois_obj, players):
        tournois_obj.bind_players(players)

    def display_match_of_round(self, round):
        for match in round.matchs:
            self.score.display_match(match)

    def generate_first_round(self, tournois_obj):
        first_round_list = Suisse().generate_first_round(tournois_obj.players_list)
        self.round = Round().create_round('Round 1')
        for players in first_round_list:
            match = Match().create_match(players[0], 0, players[1], 0)
            self.round.add_match_to_round(match)
        tournois_obj.add_round(self.round)
        RoundView().start_new_round(self.round)
        self.display_match_of_round(self.round)

    def generate_next_round(self, previous_round, tournois_obj):
        if len(tournois_obj.round_list) < DEFAULT_TOUR_NUMBER:

            match_list = Suisse().generate_next_round(previous_round, tournois_obj)

            self.round = Round().create_round(f'Round {len(tournois_obj.round_list)+1}')
            RoundView().start_new_round(self.round)
            for match in match_list:
                formated_match = Match().create_match(match[0][0], match[0][1], match[1][0], match[1][1])
                self.round.add_match_to_round(formated_match)
            tournois_obj.add_round(self.round)
            self.display_match_of_round(self.round)

        else:
            # fin de tournois => afficher score
            # récupérer la liste triée:
            players = Suisse().get_players_list_with_score(tournois_obj.round_list[-1])
            sorted_list = Suisse().sort_list_by_score(players)
            self.score.display_final_score(sorted_list)
            print("Fin du tournois => scores")

    def create_tournament(self):

        tournament_infos = self.tournament_view.get_tournament_info()

        self.tournois_obj = Tournament()
        self.tournois_obj.add_tournament(tournament_infos)

        # TODO : a remplacer par la liste du modèle
        self.tournaments.append(self.tournois_obj)

        # number_of_player = self.get_players_number()
        self.add_multiple_players(self.tournois_obj.number_of_players)

        # TODO : normal ?
        self.bind_player_to_tournament(self.tournois_obj, self.players)
        self.players = []
        # print(self.tournois_obj.players_list)

        self.generate_first_round(self.tournois_obj)

    def menu_principal(self):
        selected_menu = self.menu_view.display_menu()
        self.routing_menu_principal(selected_menu)

    def run(self):
        while self.running:
            self.menu_principal()
