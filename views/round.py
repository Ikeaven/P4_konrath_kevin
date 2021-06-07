""" Round View """


# from .fields import Fields
from .utilities import UtilitiesView
from .score import ScoreView

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

    def display_round(self, tournament):
        for round in tournament.round_list:
            UtilitiesView().line_separator()
            print()
            print("##################")
            print(f"---- {round.round_name} ----")
            print("##################")
            print()
            print(f"Début : {round.start_round_datetime}")
            # TODO end_round
            # print(f"end at : {round.end_round_datetime}")

            for match in round.matchs:
                ScoreView().display_match(match)
