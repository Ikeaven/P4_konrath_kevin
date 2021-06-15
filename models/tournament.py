#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tournament:

    LISTE_TOURNOIS = []

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
        cls.LISTE_TOURNOIS.append(tournament)

    def bind_players(self, players: list):
        for player in players:
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