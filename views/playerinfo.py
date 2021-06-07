"""Get player info view"""

from .utilities import UtilitiesView
from .fields import Fields


class GetPlayerInfoView:

    def __init__(self):
        self.utilities = UtilitiesView()
        self.fields = Fields()

    def get_player_info(self, num_player):
        self.utilities.line_separator()
        print("Player", num_player)
        last_name = self.fields.input_text_field('Nom du joueur :')
        first_name = self.fields.input_text_field('Prénom du joueur :')
        date_of_birth = self.fields.input_date_field("date d'anniversaire (jj/mm/aaaa): ")
        sex = self.fields.input_sex_field("sexe du joueur [M] / [F] : ")
        ranking = self.fields.input_digit_field("Score du joueur : ")
        self.utilities.line_separator()
        return {"last_name": last_name,
                "first_name": first_name,
                "date_of_birth": date_of_birth,
                "sex": sex,
                "ranking": ranking}

    # def how_many_players(self):
    #     player_number = input(f"Combien de joueurs pour le tournois ? (si vide default {}): ")
    #     return player_number

    def prompt_players_list(self, players):
        self.utilities.line_separator()

        for index, player in enumerate(players):
            print(f'index : [{index}]')
            print(f'{player.first_name} {player.last_name}')
            print(f"date of birth: {player.date_of_birth}")
            print(f"sex: {player.sex}")
            print(f"ranking : {player.ranking}")
            self.utilities.line_separator()
