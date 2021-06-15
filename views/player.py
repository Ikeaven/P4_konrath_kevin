"""Get player info view"""

from .utilities import UtilitiesView
from .fields import Fields


class PlayerView:

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
        ranking = self.fields.input_digit_field("Classement du joueur : ")
        self.utilities.line_separator()
        return {"last_name": last_name,
                "first_name": first_name,
                "date_of_birth": date_of_birth,
                "sex": sex,
                "ranking": ranking}

    # def how_many_players(self):
    #     player_number = input(f"Combien de joueurs pour le tournois ? (si vide default {}): ")
    #     return player_number

    def display_players_list(self, players:list):
        self.utilities.line_separator()

        for index, player in enumerate(players):
            print(f'index : [{index}]')
            print(f'{player.first_name} {player.last_name}')
            print(f"date of birth: {player.date_of_birth}")
            print(f"sex: {player.sex}")
            print(f"ranking : {player.ranking}")
            self.utilities.line_separator()

    def update_ranking(self, player:object):
        print(f'classement avant mise à jour : {player.ranking}')
        new_ranking = self.fields.input_digit_field('Nouveau classement :')
        return new_ranking

    def update_name(self, player:object):
        print(f'Prénom Nom avant mise à jour : {player.first_name} {player.last_name}')
        new_first_name = self.fields.input_text_field('Nouveau prénom :')
        new_last_name = self.fields.input_text_field('Nouveau nom :')
        return new_first_name, new_last_name

    def update_birthday(self, player:object):
        print(f'Anniversaire avant mise à jour : {player.date_of_birth}')
        new_date_of_birth = self.fields.input_date_field('Nouvelle date de naissance :')
        return new_date_of_birth
        
    def update_sex(self, player:object):
        print(f'Sexe du joueur avant mise à  jour : {player.sex}')
        new_sex = self.fields.input_sex_field('Nouveau sexe [M] / [F] : ')
        return new_sex