#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO : Module summary
"""

import time

from typing import List

from models.player import Player
from models.tournament import Tournament

from views.utilities import UtilitiesView

from utilities.checker import checker_text_field, checker_menu, checker_digit_field
from utilities.checker import checker_digit_or_empy_default_field


class Controller:
    """Main Controller."""

    DEFAULT_TOUR_NUMBER = 4

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

    def prompt_base_menu(self):
        selected_menu = self.menu_view.prompt_menu()
        self.routing_menu(selected_menu)

    def routing_menu(self, selected_menu):
        if selected_menu == '1':
            # Créer un nouvau tournoi
            self.create_tournament()

        elif selected_menu == '2':
            # Éditer un tournoi
            print("editin de tournoi")

        elif selected_menu == '3':
            # Editer joueur
            self.get_player_info_view.prompt_players_list(self.players)
        
        elif selected_menu == '4':
            # Afficher les joueurs
            self.get_all_players_from_model()

        elif selected_menu == '5':
            # Afficher les tournois
            pass
            
        elif selected_menu == '9':
            # stop
            self.running = False
        else:
            # Choix n'est pas dans les propositions du menu
            self.utilities_view.prompt_error()

    def get_all_players_from_model(self):
        self.all_players = Player().get_all_players()
        self.get_player_info_view.prompt_players_list(self.all_players)
        

    def add_multiple_players(self, players_number):
        for num_player in range(int(players_number)):
            player_info = self.get_player_info_view.get_player_info(num_player + 1)
            player_obj = Player()
            player_obj.add_player(player_info)
            self.players.append(player_obj)

    @checker_digit_field
    def get_players_number(self):
        return self.get_player_info_view.how_many_players()

    @checker_menu(1, 3)
    def get_time_controle(self):
        return self.get_tournament_info_view.get_time_controller()

    @checker_text_field
    def get_name_tournament(self):
        return self.get_tournament_info_view.get_name_tournament()

    @checker_text_field
    def get_location_tournament(self):
        return self.get_tournament_info_view.get_location_tournament()

    @checker_digit_or_empy_default_field(DEFAULT_TOUR_NUMBER)
    def get_tour_number(self):
        return self.get_tournament_info_view.get_tour_number(self.DEFAULT_TOUR_NUMBER)

    @checker_text_field
    def get_description(self):
        return self.get_tournament_info_view.get_description()
    
    def bind_player_to_tournament(self, tournois_obj, players):
        tournois_obj.bind_players(players)

    def create_tournament(self):
        name_tournament = self.get_name_tournament()
        location_tournament = self.get_location_tournament()
        start_date = time.localtime()
        end_date = "not finished"
        tour_number = self.get_tour_number()
        time_controller = self.get_time_controle()
        description = self.get_description()

        tournament_info = {
            "name_tournament": name_tournament,
            "location_tournament": location_tournament,
            "start_date": start_date,
            "end_date": end_date,
            "tour_number": tour_number,
            "time_controller": time_controller,
            "description": description
        }

        self.tournois_obj = Tournament()
        self.tournois_obj.add_tournament(tournament_info)

        # TODO : a remplacer par la liste du modèle 
        self.tournaments.append(self.tournois_obj)

        number_of_player = self.get_players_number()
        self.add_multiple_players(number_of_player)

        # TODO : normal ? 
        self.bind_player_to_tournament(self.tournois_obj, self.players)

    def run(self):
        while self.running:
            self.prompt_base_menu()
