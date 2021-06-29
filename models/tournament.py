#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tournament:

    TOURNAMENT_LIST = []

    def __init__(self):
        pass

    def add_tournament(self, tournois_infos):
        for attr_name, attr_value in tournois_infos.items():
            setattr(self, attr_name, attr_value)
        self.players_list = []
        self.round_list = []
        self.append_tournois(self)

    @classmethod
    def append_tournois(cls, tournament):
        cls.TOURNAMENT_LIST.append(tournament)

    def bind_multiple_players(self, players: list):
        for player in players:
            self.players_list.append(player)

    def bind_player(self, player):
        self.players_list.append(player)

    def add_round(self, round: object):
        self.round_list.append(round)

    def update_name(self, new_tournament_name):
        self.tournament_name = new_tournament_name

    def update_description(self, new_description):
        self.description = new_description

    def update_time_controller(self, new_time_controller):
        self.time_controller = new_time_controller

    def update_location(self, new_location):
        self.location = new_location

    def update_start_date(self, new_strat_date):
        self.start_date = new_strat_date

    def update_end_date(self, new_end_date):
        self.end_date = new_end_date

    def set_final_score(self, sorted_list):
        self.final_score = sorted_list
