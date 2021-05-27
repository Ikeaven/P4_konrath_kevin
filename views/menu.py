#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MenuView: 

    def prompt_menu(self):
        print("[1] Créer un nouveau tournois")
        print("[2] Modifier le classement d'un joueur")
        print("[5] Quitter")
        menu_value = input('entrer le numéro du menu :')
        if menu_value not in ('1','2','5'):
            return None
        return menu_value

    def create_tournament(self):
        name_tournament = input("Nom du tournois : ")
        location_tournament = input ("Lieu du tournois : ")
        start_date = input("Date de début du tournois : ")
        end_date = input("Date de fin du tournois : ")
        tour_number = input("Nombre de tour (si champ vide, 4 par défaut) : ")
        time_controller = input("[1] buller / [2] blitz / [3] coup rapide : ")
        description = input("Description du tournois : ")
        return (name_tournament, location_tournament, start_date, end_date, tour_number,
            time_controller, description)