""" Import from TinyDB / Export to TinyDB """

from tinydb import TinyDB

# TODO nom db dans config
db = TinyDB('db.json')
players_table = db.table('players')
tournaments_table = db.table('tournaments')

def clear_db(table):
    table.truncate()

def insert_players_to_db(players):
    players_table.insert_multiple(players)

def insert_tournaments_to_db(tournaments):
    tournaments_table.insert_multiple(tournaments)


# clear_db(players_table)
# clear_db(tournaments_table)
