

from .utilities import UtilitiesView
from .fields import Fields

from .match import MatchView


class ScoreView:

    def __init__(self):
        self.match_view = MatchView()

    def update_score(self, match):
        self.match_view.display_match(match)
        print('[0] Match null')
        print('[1] Player 1 est gagnant')
        print('[2] Player 2 est gagnant')
        selected_menu = int(Fields().input_winner('Qui est le gagnant ?'))
        UtilitiesView().line_separator()
        return selected_menu

    def display_final_score(self, sorted_list):
        print("\n###################")
        print("### SCORE FINAL ###")
        print("###################")
        for i, player in enumerate(sorted_list):
            UtilitiesView().line_separator()
            print(f"{i+1}: {player[0].first_name} {player[0].last_name} ")
            print(f"Clanssement : {player[0].ranking}")
            print(f"Score : {player[1]}")
            UtilitiesView().line_separator()
