""" Match View Module """

import pandas as pd
from .utilities import UtilitiesView


class MatchView:

    def display_match(self, match):
        """Print all match informations in a pandas DataFrame

        Args:
            match (obj): Match instance
        """
        UtilitiesView().line_separator()
        print()
        data = {
                'Joueur 1': f'{match.player1.first_name} {match.player1.last_name} ',
                'Classement joueur 1': f'{match.player1.ranking}',
                'Score joueur 1': match.score_player1,
                'VS': '|',
                'Joueur 2': f'{match.player2.first_name} {match.player2.last_name} ',
                'Classement joueur 2': f'{match.player2.ranking} ',
                'Score joueur 2':  match.score_player2
                }
        with pd.option_context('display.colheader_justify', 'center'):
            df = pd.DataFrame(data=data, index=['Match =>'])
            print(df)
        UtilitiesView().line_separator()
