"""Get player info view"""

from models.player import Player
from .utilities import UtilitiesView
from .fields import Fields


class PlayerView:

    def __init__(self):
        self.utilities = UtilitiesView()
        self.fields = Fields()

    def get_player_info(self, num_player=len(Player.LIST_PLAYERS)) -> dict:
        """Ask to user the player's informations

        Args:
            num_player (int, optional): player number in a tournament or in all players.
                Defaults to len(Player.LIST_PLAYERS).

        Returns:
            dict: player information
        """
        self.utilities.line_separator()
        print("Player", num_player)
        last_name = self.fields.input_text_field('Nom du joueur :')
        first_name = self.fields.input_text_field('Prénom du joueur :')
        date_of_birth = self.fields.input_date_field("date d'anniversaire (jj/mm/aaaa): ")
        sex = self.fields.input_sex_field("sexe du joueur [M] / [F] : ")
        ranking = int(self.fields.input_digit_field("Classement du joueur : "))
        self.utilities.line_separator()
        return {"last_name": last_name,
                "first_name": first_name,
                "date_of_birth": date_of_birth,
                "sex": sex,
                "ranking": ranking}

    # def how_many_players(self):
    #     player_number = input(f"Combien de joueurs pour le tournois ? (si vide default {}): ")
    #     return player_number

    def display_players_list(self, players: list):
        """Display informations about players in a list

        Args:
            players (list): list of player whose information we want to display
        """
        self.utilities.line_separator()
        if players is not None:
            for index, player in enumerate(players):
                print(f'\nindex : [{index}]')
                print(f'{player.first_name} {player.last_name}')
                print(f"Date de naissance : {player.date_of_birth}")
                print(f"Sexe : {player.sex}")
                print(f"Classement : {player.ranking}")
                self.utilities.line_separator()
        else:
            pass

    def update_ranking(self, player: object):
        """Ask to user to type a new ranking for a player

        Args:
            player (object): Player instance to update

        Returns:
            [str]: it's a digit in a string, new ranking
        """
        print(f'\nlassement avant mise à jour : {player.ranking}')
        new_ranking = self.fields.input_digit_field('Nouveau classement :')
        return new_ranking

    def update_name(self, player: object):
        """Ask to user to type a new First_Name & Last name for a player

        Args:
            player (object): PLayer instance to update

        Returns:
            tuple: new_first_name, new_last_name
        """
        print(f'\nPrénom Nom avant mise à jour : {player.first_name} {player.last_name}')
        new_first_name = self.fields.input_text_field('Nouveau prénom :')
        new_last_name = self.fields.input_text_field('Nouveau nom :')
        return new_first_name, new_last_name

    def update_birthday(self, player: object):
        """Ask to user to type a new date of birth for a player

        Args:
            player (object): Player instance to update

        Returns:
            str: new date of birth
        """
        print(f'\nAnniversaire avant mise à jour : {player.date_of_birth}')
        new_date_of_birth = self.fields.input_date_field('Nouvelle date de naissance :')
        return new_date_of_birth

    def update_sex(self, player: object):
        """Ask to user to type a new sex for a player

        Args:
            player (object): Player instcance to update

        Returns:
            str: new sex ('M' or 'F')
        """
        print(f'\nSexe du joueur avant mise à  jour : {player.sex}')
        new_sex = self.fields.input_sex_field('Nouveau sexe [M] / [F] : ')
        return new_sex
