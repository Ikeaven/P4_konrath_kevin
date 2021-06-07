""" Round View """


# from .fields import Fields
from .utilities import UtilitiesView


class RoundView:
    def dispalay_start_time(self):
        pass

    def display_stop_time(self, round):
        print(f'Arrêt à : {round.end_round_datetime}')

    def start_new_round(self, round):
        UtilitiesView().line_separator()
        print()
        print("Un nouveau round a été généré automatiquement, le tournoi n'est pas terminé !!")
        print(f"Voici les matchs du {round.round_name} : ")
