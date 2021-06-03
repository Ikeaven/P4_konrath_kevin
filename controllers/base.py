#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO : Module summary
"""

import time
import random

from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from views.utilities import UtilitiesView

from utilities.checker import checker_text_field, checker_menu, checker_digit_field
from utilities.checker import checker_digit_or_empy_default_field

from paires.suisse import Suisse


class Controller:
    """Main Controller."""

    def __init__(self, menu_view, get_player_info_view, get_tournament_info_view):
        # models
        self.players: List[Player] = []
        self.tournaments: List[Tournament] = []

        # views
        self.menu_view = menu_view
        self.get_player_info_view = get_player_info_view
        self.get_tournament_info_view = get_tournament_info_view
        self.utilities_view = UtilitiesView()

        self.running = True

    def routing_menu(self, selected_menu):
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
            self.get_player_info_view.prompt_players_list(self.players)
        
        elif selected_menu == '4':
            # Afficher les joueurs
            self.get_all_players_from_model()

        elif selected_menu == '5':
            # Afficher les tournois
            self.get_tournament_info_view.prompt_tournament_list(Tournament().LISTE_TOURNOIS)

        elif selected_menu == '6':
            # fin de round
            try:
                self.round.end_round()
                # TODO : passer à la view 
                print(f'end at : {self.round.end_round_datetime}')
                # aller à la mise à jour des scores de chaque match 
                # lancer le round suivant ou terminer le tournois
            except AttributeError:
                self.utilities_view.prompt_error()


        elif selected_menu == '8':
            # TEST générer tournois auto    
            self.TEST_import_auto_tournoi()

        elif selected_menu == '9':
            # stop
            self.running = False
        else:
            # Choix n'est pas dans les propositions du menu
            self.utilities_view.prompt_error()

    def get_all_players_from_model(self):
        self.all_players = Player().get_all_players()
        self.get_player_info_view.prompt_players_list(self.all_players)
    
    def edit_tournament(self):
        self.get_tournament_info_view.prompt_tournament_list(Tournament().LISTE_TOURNOIS)
        item_index = self.menu_view.select_item()
        tournoi = Tournament().LISTE_TOURNOIS[int(item_index)]
        print(tournoi.tournament_name)


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
        self.bind_player_to_tournament(self.tournois_obj, self.players)
        self.generate_first_round(self.tournois_obj)



    # AUTO REMPLISSAGE POUR TESTER PLUS FACILEMENT 
    # TODO : A SUPPRIMER
    def TEST_import_auto_players(self, players_number):
        for num_player in range(int(players_number)):
            player_infos = {
                "last_name": f'Nom joueur {str(num_player)}',
                "first_name": f'Prénom joueur {str(num_player)}',
                "date_of_birth": f'{random.randint(10, 28)}/{random.randint(10, 12)}/{random.randint(1950, 2021)}',
                "sex": 'M' if random.randint(0,1) else 'F',
                "ranking": random.randint(100, 3000)}
            player_obj = Player()
            player_obj.add_player(player_infos)
            self.players.append(player_obj)


    def add_multiple_players(self, players_number): 
        # TODO REMPLISSAGE AUTO A SUPPRIMER => POUR TEST 
        menu = self.menu_view.test_import_auto()
        if menu == '1':
            self.TEST_import_auto_players(players_number)
        elif menu == '2':
            for num_player in range(int(players_number)):
                selected_menu = self.menu_view.prompt_menu_add_player()
                if selected_menu == '1':
                    self.get_all_players_from_model()
                    # selectionner le joueur à ajouter
                elif selected_menu == '2':
                    player_info = self.get_player_info_view.get_player_info(num_player + 1)
                    player_obj = Player()
                    player_obj.add_player(player_info)
                    self.players.append(player_obj)
                else: 
                    self.utilities_view.prompt_error()
        else:
            self.utilities_view.prompt_error()
    
    def bind_player_to_tournament(self, tournois_obj, players):
        tournois_obj.bind_players(players)

    def generate_first_round(self, tournois_obj):
        first_round_list = Suisse().generate_first_round(tournois_obj.players_list)
        self.round = Round().create_round('Round 1')
        for players in first_round_list: 
            match = Match().create_match(players[0], 0, players[1], 0)
            self.round.add_match_to_round(match)
        tournois_obj.add_round(self.round)
        

    def create_tournament(self):

        tournament_infos = self.get_tournament_info_view.get_tournament_info()

        self.tournois_obj = Tournament()
        self.tournois_obj.add_tournament(tournament_infos)

        # TODO : a remplacer par la liste du modèle 
        self.tournaments.append(self.tournois_obj)

        # number_of_player = self.get_players_number()
        self.add_multiple_players(self.tournois_obj.number_of_players)

        # TODO : normal ? 
        self.bind_player_to_tournament(self.tournois_obj, self.players)
        # print(self.tournois_obj.players_list)

        self.generate_first_round(self.tournois_obj)

    def run(self):
        while self.running:
            selected_menu = self.menu_view.prompt_menu()
            self.routing_menu(selected_menu)
