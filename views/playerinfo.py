"""Get player info view"""

from .utilities import UtilitiesView

class GetPlayerInfoView:

    def __init__(self):
        self.utilities = UtilitiesView()
        
    def get_player_info(self, num_player):
        self.utilities.line_separator()
        print("Player", num_player)
        last_name = input("Nom du joueur : ")
        first_name = input("Prénom du joueur : ")
        date_of_birth = input("date d'anniversaire : ")
        sex = input("sexe du joueur [M] / [F] : ")
        ranking = input("score du joueur : ")
        self.utilities.line_separator()
        return {"last_name" : last_name,
            "first_name" : first_name,
            "date_of_birth" : date_of_birth,
            "sex" : sex,
            "ranking" : ranking}
    
    def how_many_players(self):
        player_number = input("Combien de joueurs pour le tournois ? : ")
        return player_number

    def prompt_players_list(self, players):
        for player in players:
            print(f'{player.first_name}, {player.last_name}')