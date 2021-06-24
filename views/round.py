""" Round View """


# from .fields import Fields
from views.match import MatchView
from .utilities import UtilitiesView


class RoundView:
    def display_start_time(self):
        pass

    def display_stop_time(self, round):
        print()
        print(f'Round arrété à : {round.end_round_datetime}')

    def start_new_round(self, round):
        UtilitiesView().line_separator()
        print()
        print("Un nouveau round a été généré automatiquement, le tournoi n'est pas terminé !!")
        print(f"Voici les matchs du {round.round_name} : ")

    def display_round(self, tournament, show_match=False):
        for round in tournament.round_list:
            UtilitiesView().line_separator()
            print()
            print("##################")
            print(f"---- {round.round_name} ----")
            print("##################")
            print()
            print(f"Début : {round.start_round_datetime}")
            print(f"Fin : {round.end_round_datetime}")
            if show_match:
                for match in round.matchs:
                    MatchView().display_match(match)
