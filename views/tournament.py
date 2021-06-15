""" Get tournament infos view"""

from config import DEFAULT_TOUR_NUMBER, DEFAULT_PLAYERS_NUMBER

from .utilities import UtilitiesView
from .fields import Fields


class TournamentView:

    def __init__(self):
        self.utilities = UtilitiesView()
        self.fields = Fields()

    def get_tournament_info(self):
        # TODO : date de début
        # TODO : date de fin si plusieurs jours
        tournament_name = self.fields.input_text_field("Nom du tournoi : ")
        location = self.fields.input_text_field("Lieu du tournoi : ")
        time_controller = self.fields.input_time_controler("[1] bullet / [2] blitz / [3] coup rapide : ")
        description = self.fields.input_text_field("Description du tournois : ")
        message_nombre_tour = f"Nombre de tour (si champ vide, {DEFAULT_TOUR_NUMBER} par défaut) : "
        tour_number = self.fields.input_tour_number(message_nombre_tour)
        message_nombre_joueur = f'Nombre de joueurs du tournoi (si vide, default {DEFAULT_PLAYERS_NUMBER}) : '
        number_of_players = self.fields.input_number_of_players(message_nombre_joueur)
        tournament_infos = {'tournament_name': tournament_name,
                            'location': location,
                            'tour_number': tour_number,
                            'time_controller': time_controller,
                            'number_of_players': number_of_players,
                            'description': description}
        return tournament_infos

    # def get_name_tournament(self):
    #     return input("Nom du tournoi : ")

    # def get_location_tournament(self):
    #     return input("Lieu du tournois : ")

    # def get_tour_number(self, default):
    #     return input(f"Nombre de tour (si champ vide, {DEFAULT_TOUR_NUMBER} par défaut) : ")

    # def get_time_controller(self):
    #     return input("[1] bullet / [2] blitz / [3] coup rapide : ")

    # def get_description(self):
    #     return input("Description du tournois : ")

    def display_tournament_list(self, tournaments_list):
        self.utilities.line_separator()

        for index, tournament in enumerate(tournaments_list):
            print(f'Index du tournoi : [{index}]')
            print(f'{tournament.tournament_name}')
            print(f'{tournament.location}')
            self.utilities.line_separator()

    def display_tournoi(self, tournoi):
        pass


    def update_tournament_name(self, tournament):
        print(f'Nom avant mise à jour : {tournament.tournament_name}')
        new_tournament_name = self.fields.input_text_field('Nouveau nom du tournoi : ')
        return new_tournament_name

    def update_tournament_description(self, tournament):
        print(f'Description avant mise à jour : {tournament.description}')
        new_description = self.fields.input_text_field('Nouvelle description du tournoi :')
        return new_description

    def update_time_controller(self, tournament):
        print(f'Controller avant mise à jour : {tournament.time_controller}')
        new_time_controller = self.fields.input_time_controler('Nouveau controller de temps [1] bullet / [2] blitz / [3] coup rapide :')
        return new_time_controller