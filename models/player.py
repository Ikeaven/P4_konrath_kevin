""" Player model """


class Player:

    LIST_PLAYERS = []

    def add_player(self, player_info):
        """Add new player

        Args:
            player_info (dict): players inforamtions
        """
        for attr_name, attr_value in player_info.items():
            setattr(self, attr_name, attr_value)
        self.append_player(self)

    def update_ranking(self, new_ranking: int):
        """Update players ranking

        Args:
            new_ranking (int): new ranking
        """
        self.ranking = new_ranking

    def update_name(self, new_first_name, new_last_name):
        """Update player's name

        Args:
            new_first_name (str): First name
            new_last_name (str): Last name
        """
        self.first_name = new_first_name
        self.last_name = new_last_name

    def update_birthday(self, new_date_of_birth):
        """Update player's birthday

        Args:
            new_date_of_birth (str): date of birth
        """
        self.date_of_birth = new_date_of_birth

    def update_sex(self, new_sex):
        """Update player's sex

        Args:
            new_sex (str): sex, 'M' or 'F'
        """
        self.sex = new_sex

    @classmethod
    def append_player(cls, player):
        """Add player instance to LIST_PLAYERS

        Args:
            player (obj): Player instance
        """
        cls.LIST_PLAYERS.append(player)

    @classmethod
    def get_all_players(cls) -> list or None:
        """Get all players instances.

        Returns:
            list or None: All players instances or None if LIST_PLAYERS is empty
        """
        if cls.LIST_PLAYERS == []:
            return None
        else:
            return cls.LIST_PLAYERS

    @classmethod
    def get_player_by_id(cls, player_id: str) -> object:
        """Get a player instance from id

        Args:
            player_id (str): player id : uuid

        Returns:
            object: Player instance correspond to player_id
        """
        for player in cls.LIST_PLAYERS:
            if player.id == player_id:
                return player
