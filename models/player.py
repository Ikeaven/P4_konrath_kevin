""" Player model """


class Player:

    LIST_PLAYERS = []

    def add_player(self, player_info):
        for attr_name, attr_value in player_info.items():
            setattr(self, attr_name, attr_value)
        self.append_player(self)

    def update_ranking(self, new_ranking: int):
        self.ranking = new_ranking

    def update_name(self, new_first_name, new_last_name):
        self.first_name = new_first_name
        self.last_name = new_last_name

    def update_birthday(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth

    def update_sex(self, new_sex):
        self.sex = new_sex

    @classmethod
    def append_player(cls, player):
        cls.LIST_PLAYERS.append(player)

    @classmethod
    def get_all_players(cls) -> list or None:
        if cls.LIST_PLAYERS == []:
            return None
        else:
            return cls.LIST_PLAYERS

    @classmethod
    def get_player_by_id(cls, player_id: str) -> object:
        for player in cls.LIST_PLAYERS:
            if player.id == player_id:
                return player
