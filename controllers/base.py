#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO : Module summary
"""

from typing import List

from models.player import Player
from models.tournament import Tournament
class Controller:
    """Main Controller."""

    def __init__(self, view, checker):
        # models
        self.players : List[Player] = []
        self.tournaments : List[Tournament] = []
        
        # views 
        self.view = view

        # utilities checker
        self.checker = checker

    def prompt_base_menu(self):
        selected_menu = self.view.prompt_menu()
        self.routing_menu(selected_menu)
        
    def routing_menu(self, selected_menu):
        if selected_menu == '1':
            #Créer un nouveau tournois
            self.create_tournament()

        elif selected_menu == '2':
            #Modifier le classement d'un joueur
            print("midif classement joueur")
        else:
            pass

    def get_players(self, players_number):
        for num_player in range(int(players_number)):
            self.view.get_player_info()

    def create_tournament(self):
        self.tournaments.append(Tournament(self.view.create_tournament()))
        print(self.tournaments[0].__dict__)
        # print(self.view.create_tournament())
        
        player_is_not_enter = True
        while player_is_not_enter:
            players_number = self.view.how_many_players()
            if self.checker.string_is_a_number(players_number):
                self.get_players(players_number)
                player_is_not_enter = False
        

    def run(self):
        self.prompt_base_menu()