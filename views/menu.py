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
    
    def how_many_players(self):
        player_number = input("Combien de joueurs pour le tournois ? : ")
        return player_number

    def separator(self):
        print("_________________________________________")

    def get_player_info(self):
        last_name = input("Nom du joueur : ")
        first_name = input("Prénom du joueur : ")
        date_of_birth = input("date d'anniversaire : ")
        sex = input("sexe du joueur [M] / [F] : ")
        ranking = input("score du joueur : ")
        self.separator()
        return (last_name, first_name, date_of_birth, sex, ranking)

    def create_tournament(self):
        #TODO : exploser la fonction dans plusieurs fonction et check des inputs
        name_tournament = input("Nom du tournois : ")
        location_tournament = input ("Lieu du tournois : ")
        start_date = input("Date de début du tournois : ")
        end_date = input("Date de fin du tournois : ")
        tour_number = input("Nombre de tour (si champ vide, 4 par défaut) : ")
        time_controller = input("[1] buller / [2] blitz / [3] coup rapide : ")
        description = input("Description du tournois : ")
        return {"name_tournament" : name_tournament, 
                "location_tournament" : location_tournament,
                "start_date" : start_date,
                "end_date" : end_date,
                "tour_number" : tour_number,
                "time_controller" : time_controller,
                "description" : description}