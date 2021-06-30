#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Tournament:

    TOURNAMENT_LIST = []

    def add_tournament(self, tournois_infos):
        """Create a tournament instance

        Args:
            tournois_infos ([type]): [description]
        """
        for attr_name, attr_value in tournois_infos.items():
            setattr(self, attr_name, attr_value)
        self.players_list = []
        self.round_list = []
        self.append_tournois(self)

    @classmethod
    def append_tournois(cls, tournament):
        """Add a tournament instance to TOURNAMENT_LIST

        Args:
            tournament (obj): Tournament instance
        """
        cls.TOURNAMENT_LIST.append(tournament)

    def bind_multiple_players(self, players: list):
        """Link a list of players to the tournament

        Args:
            players (list): list of PLayer instances
        """
        for player in players:
            self.players_list.append(player)

    def bind_player(self, player):
        """Link a single player to the tournament

        Args:
            player (obj): Player instance to bind to the tournament
        """
        self.players_list.append(player)

    def add_round(self, round: object):
        """Link a round to the tournament

        Args:
            round (object): Round instance
        """
        self.round_list.append(round)

    def update_name(self, new_tournament_name):
        """Update tournament name

        Args:
            new_tournament_name (str): new tournament name
        """
        self.tournament_name = new_tournament_name

    def update_description(self, new_description):
        """Update tournament description

        Args:
            new_description (str): description
        """
        self.description = new_description

    def update_time_controller(self, new_time_controller):
        """Update ime controller

        Args:
            new_time_controller (str): new time controller, it's an integer in a string.
        """
        self.time_controller = new_time_controller

    def update_location(self, new_location):
        """Update location

        Args:
            new_location (str): new location
        """
        self.location = new_location

    def update_start_date(self, new_strat_date):
        """Update start date of tournament

        Args:
            new_strat_date (str): start date
        """
        self.start_date = new_strat_date

    def update_end_date(self, new_end_date):
        """Updtae end date

        Args:
            new_end_date (str): end date
        """
        self.end_date = new_end_date

    def set_final_score(self, sorted_list):
        """Set final score to tournament

        Args:
            sorted_list (list): list of players with score sorted by score and ranking
        """
        self.final_score = sorted_list
