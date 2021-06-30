

from .utilities import UtilitiesView
from .fields import Fields

from .match import MatchView


class ScoreView:

    def __init__(self):
        self.match_view = MatchView()

    def update_score(self, match):
        """Ask player who is the winner

        Args:
            match (obj): Match instance

        Returns:
            str: selected_menu, user choice
        """
        self.match_view.display_match(match)
        print('[0] Match null')
        print('[1] Player 1 est gagnant')
        print('[2] Player 2 est gagnant')
        selected_menu = int(Fields().input_winner('Qui est le gagnant ?'))
        UtilitiesView().line_separator()
        return selected_menu

    def display_final_score(self, sorted_list):
        """Display score from a list of player with score

        Args:
            sorted_list (list[[player, score], [player, score]]): list of player with score
        """
        print("\n###################")
        print("### SCORE FINAL ###")
        print("###################")
        for i, player in enumerate(sorted_list):
            UtilitiesView().line_separator()
            print(f"{i+1}: {player[0].first_name} {player[0].last_name} ")
            print(f"Clanssement : {player[0].ranking}")
            print(f"Score : {player[1]}")
            UtilitiesView().line_separator()
