""" Player model """
class Player:

    LIST_PLAYERS = []

    def add_player(self, player_info):
        for attr_name, attr_value in player_info.items():
            setattr(self, attr_name, attr_value)
        self.append_player(self)

    @classmethod
    def append_player(cls, player):
        cls.LIST_PLAYERS.append(player)

    def get_all_players(self):
        return self.LIST_PLAYERS
