""" Import from TinyDB / Export to TinyDB """


from tinydb import TinyDB, where

from config import DB_NAME



class Database:

    def __init__(self):
        self.db = TinyDB(DB_NAME)
        # self.clear_db()
        self.players_table = self.db.table('players')
        self.tournaments_table = self.db.table('tournaments')
        self.rounds_table = self.db.table('rounds')
        self.matchs_table = self.db.table('matchs')

    def clear_db(self, ):
        # self.db.truncate()
        # TODO : supprimer la table et réinitialiser les ID de table
        self.db.drop_tables()

    def insert_players_to_db(self, players):
        self.players_table.insert_multiple(players)

    def insert_rounds_to_db(self, rounds):
        self.rounds_table.insert_multiple(rounds)

    def insert_matchs_to_db(self, matchs):
        self.matchs_table.insert_multiple(matchs)

    def insert_tournaments_to_db(self, tournaments):
        self.tournaments_table.insert_multiple(tournaments)

    def get_all_players(self) -> list:
        players = self.db.table('players')
        return players.all()

    def get_all_tournaments(self) -> list:
        tournaments = self.db.table('tournaments')
        return tournaments.all()

    def get_all_rounds_of_tournament(self, tournament_id: str) -> list:
        tournament = self.tournaments_table.search(where('id') == tournament_id)
        rounds = []
        for round_id in tournament[0]['round_list']:
            round_dict = self.rounds_table.search(where('id') == round_id)
            rounds.append(round_dict[0])
        return rounds

    def get_all_matchs_of_round(self, round_id: int) -> list:
        round = self.rounds_table.search(where('id') == round_id)
        matchs = []
        for match_id in round[0]['matchs']:
            match_dict = self.matchs_table.search(where('id') == match_id)
            matchs.append(match_dict[0])
        return matchs
