""" Get tournament infos view"""

from .utilities import UtilitiesView

class GetTournamentInfoView:

    def __init__(self):
        self.utilities = UtilitiesView()

    def get_name_tournament(self):
        return input("Nom du tournois : ")

    def get_location_tournament(self):
        return input("Lieu du tournois : ")

    def get_tour_number(self):
        return input("Nombre de tour (si champ vide, 4 par défaut) : ")

    def get_time_controller(self):
        return input("[1] bullet / [2] blitz / [3] coup rapide : ")

    def get_description(self):
        return input("Description du tournois : ")
