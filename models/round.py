""" Round model """
from uuid import uuid1
from datetime import datetime


class Round:

    def __init__(self):
        self.end_round_datetime = 'Round en cours'

    def create_round(self, round_name):
        self.id = str(uuid1())
        self.round_name = round_name
        self.matchs = []
        return self

    def add_match_to_round(self, match):
        self.matchs.append(match)
        self.start_round()

    def start_round(self):
        self.start_round_datetime = datetime.now()

    def stop_round(self):
        self.end_round_datetime = datetime.now()

    # update date -> début et fin si besoin
