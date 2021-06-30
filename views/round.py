""" Round View """


# from .fields import Fields
from views.match import MatchView
from .utilities import UtilitiesView


class RoundView:
    def display_stop_time(self, round):
        """Display stop time for a round

        Args:
            round (object): Round instance
        """
        print()
        print(f'Round arrété à : {round.end_round_datetime}')

    def start_new_round(self, round):
        """Display round name for a new round

        Args:
            round (object): Round instance
        """
        UtilitiesView().line_separator()
        print()
        print("Un nouveau round a été généré automatiquement, le tournoi n'est pas terminé !!")
        print(f"Voici les matchs du {round.round_name} : ")

    def display_round(self, tournament, show_match=False):
        """Display all rounds in a tournamentself.

        Args:
            tournament (object): Tournament instance
            show_match (bool, optional): if true, display all matchs too. Defaults to False.
        """
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
