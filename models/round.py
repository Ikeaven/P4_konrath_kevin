""" Round model """
from uuid import uuid1
from datetime import datetime


class Round:

    ROUND_LIST = []

    def __init__(self):
        self.end_round_datetime = 'Round en cours'

    def create_round(self, round_name):
        self.id = str(uuid1())
        self.round_name = round_name
        self.matchs = []
        self.add_round_to_globale_list()
        return self

    def load_round(self, round_info: dict):
        self.id = round_info['id']
        self.round_name = round_info['round_name']
        self.start_round_datetime = round_info['start_round_datetime'] 
        self.end_round_datetime = round_info['end_round_datetime']
        self.matchs = []
        self.add_round_to_globale_list()
        return self

    def add_round_to_globale_list(self):
        self.ROUND_LIST.append(self)

    def add_match_to_round(self, match):
        self.matchs.append(match)
        self.start_round()

    def start_round(self):
        self.start_round_datetime = datetime.now()

    def stop_round(self):
        self.end_round_datetime = datetime.now()

    @classmethod
    def find_round_by_id(cls, round_id: str) -> object:
        for round in cls.ROUND_LIST:
            if round.id == round_id:
                return round


    # update date -> début et fin si besoin
