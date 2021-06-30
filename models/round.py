""" Round model """
from uuid import uuid1
from datetime import datetime


class Round:

    ROUND_LIST = []

    def __init__(self):
        """init Round and set an end round datetime
        """
        self.end_round_datetime = 'Round en cours'

    def create_round(self, round_name):
        """Create a round

        Args:
            round_name (str): round name

        Returns:
            obj: Round instance
        """
        self.id = str(uuid1())
        self.round_name = round_name
        self.matchs = []
        self.add_round_to_globale_list()
        return self

    def load_round(self, round_info: dict):
        """Load round from database informations

        Args:
            round_info (dict): round informations

        Returns:
            object: Round instance
        """
        self.id = round_info['id']
        self.round_name = round_info['round_name']
        self.start_round_datetime = round_info['start_round_datetime']
        self.end_round_datetime = round_info['end_round_datetime']
        self.matchs = []
        self.add_round_to_globale_list()
        return self

    def add_round_to_globale_list(self):
        """Add dround instance to ROUND_LIST
        """
        self.ROUND_LIST.append(self)

    def add_match_to_round(self, match):
        """Bind match to a round

        Args:
            match (obj): Match instance to add in matchs list
        """
        self.matchs.append(match)
        self.start_round()

    def start_round(self):
        """Set a start datetime for the round
        """
        self.start_round_datetime = datetime.now()

    def stop_round(self):
        """Set a end datetime for the round
        """
        del self.end_round_datetime
        self.end_round_datetime = datetime.now()

    @classmethod
    def find_round_by_id(cls, round_id: str) -> object:
        """Get a round with his id

        Args:
            round_id (str): round's uuid

        Returns:
            object: Round instance
        """
        for round in cls.ROUND_LIST:
            if round.id == round_id:
                return round
