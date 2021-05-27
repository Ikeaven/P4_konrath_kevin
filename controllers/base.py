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

from utilities.checker import checker_champ_descpition, checker_menu

class Controller:
    """Main Controller."""

    def __init__(self, menu_view, get_player_info_view, get_tournament_info_view, checker):
        # models
        self.players : List[Player] = []
        self.tournaments : List[Tournament] = []
        
        # views 
        self.menu_view = menu_view
        self.get_player_info_view = get_player_info_view
        self.get_tournament_info_view = get_tournament_info_view
        self.utilities_view = UtilitiesView()

        # utilities checker
        self.checker = checker

        self.running = True

    def prompt_base_menu(self):
        selected_menu = self.menu_view.prompt_menu()
        self.routing_menu(selected_menu)
        
    def routing_menu(self, selected_menu):
        if selected_menu == '1':
            #CRÉER UN NOUVEAU TOURNOI
            self.create_tournament()

        elif selected_menu == '2':
            # ÉDITER UN TOURNOI
            print("modif classement joueur")

        elif selected_menu == '3':
            self.get_player_info_view.prompt_players_list(self.players)

        elif selected_menu == '5':
            self.running = False
        else:
            self.utilities_view.prompt_error()         

    def get_players(self, players_number):
        for num_player in range(int(players_number)):
            player_info = self.get_player_info_view.get_player_info(num_player + 1)
            player_obj = Player(player_info)
            self.players.append(player_obj)
    
    def get_players_number(self):
        player_is_not_enter = True
        while player_is_not_enter:
            players_number = self.get_player_info_view.how_many_players()
            if players_number.isdigit():
                player_is_not_enter = False
            else:
                self.utilities_view.prompt_error_NaN()
        return int(players_number)
    
    def bind_player_to_tournament(self, tournois_obj, players):
        tournois_obj.bind_players(players)

    # def get_time_controle(self):
    #     while True:
    #         time_controller = self.get_tournament_info_view.get_time_controller()
    #         if time_controller.isdigit():
    #             time_controller = int(time_controller)
    #             if time_controller >= 1 and time_controller <= 3:
    #                 break    
    #             else:
    #                 self.utilities_view.prompt_error()
    #         else:
    #             self.utilities_view.prompt_error_NaN()
    #     return time_controller

    @checker_menu(1, 3)
    def get_time_controle(self):
        return self.get_tournament_info_view.get_time_controller()

    @checker_champ_descpition
    def get_name_tournament(self):
        return self.get_tournament_info_view.get_name_tournament()

    @checker_champ_descpition
    def get_location_tournament(self):
        return self.get_tournament_info_view.get_location_tournament()

    @checker_champ_descpition
    def get_description(self):
        return self.get_tournament_info_view.get_description()

  
    

    def create_tournament(self):
        #create Tournament Object and append to list 

        name_tournament = self.get_name_tournament()
        location_tournament = self.get_location_tournament()
        start_date = time.localtime()
        end_date = "not finished"
        tour_number = self.get_tournament_info_view.get_tour_number()
        time_controller = self.get_time_controle()
        description = self.get_description()

        tournament_info = {
            "name_tournament" : name_tournament,
            "location_tournament" : location_tournament,
            "start_date" : start_date,
            "end_date" : end_date,
            "tour_number" : tour_number,
            "time_controller" : time_controller,
            "description" : description
        }

        tournois_obj = Tournament(tournament_info)
        self.tournaments.append(tournois_obj)
        
        number_of_player = self.get_players_number()
        self.get_players(number_of_player)

        self.bind_player_to_tournament(tournois_obj, self.players)

    def run(self):
        while self.running:
            self.prompt_base_menu()

