#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tournament:

    LISTE_TOURNOIS = []

    def add_tournament(self, tournois_infos):
        for attr_name, attr_value in tournois_infos.items():
            setattr(self, attr_name, attr_value)
        self.players_list = []
        self.round_list = []
        self.append_tournois(self)

    @classmethod
    def append_tournois(cls, tournament):
        cls.LISTE_TOURNOIS.append(tournament)

    def bind_players(self, players):
        for player in players:
            self.players_list.append(player)
