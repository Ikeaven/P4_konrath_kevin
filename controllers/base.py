#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO : Module summary
"""

from views.menu import MenuView
from models.tournois import TournoisModel

class Controller:
    """Main Controller."""

    def __init__(self, view):
        self.view = view

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

    def create_tournament(self):
        tournament = self.view.create_tournament()
        print(tournament)

    def run(self):
        self.prompt_base_menu()