import pandas as pd
import numpy as np 

from .utilities import UtilitiesView
from .fields import Fields

class ScoreView:

    def display_match(self, match):
        UtilitiesView().line_separator()
        print()
        data = {
                'Player1': f'{match.player1.first_name} {match.player1.last_name} ',
                'Classement player 1' : f'{match.player1.ranking}',
                'Score player1': match.score_player1,
                'VS':'|',
                'Player2': f'{match.player2.first_name} {match.player2.last_name} ',
                'Classement player 2' : f'{match.player2.ranking} ',
                'Score player2':  match.score_player2
                }


        with pd.option_context('display.colheader_justify', 'center'):     
            df = pd.DataFrame(data=data, index=['Match =>'])
            print(df)
        UtilitiesView().line_separator()

        
    def update_score(self, match):
        self.display_match(match)
        print('[0] Match null')
        print('[1] Player 1 est gagnant')
        print('[2] Player 2 est gagnant')
        selected_menu = int(Fields().input_winner('Qui est le gagnant ?'))
        UtilitiesView().line_separator()
        return selected_menu
        
    def display_final_score(self, sorted_list):
        print("###################")
        print("### SCORE FINAL ###")
        print("###################")
        for i, player in enumerate(sorted_list):
            UtilitiesView().line_separator()
            print(f"{i+1}, {player[0].first_name} {player[0].last_name} ")
            print(f"ranking : {player[0].ranking}")
            print(f"score : {player[1]}")
            UtilitiesView().line_separator()
