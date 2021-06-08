""" Import from TinyDB / Export to TinyDB """

from tinydb import TinyDB

db = TinyDB('db.json')
players_table = db.table('players')

def clear_db(table):
    table.truncate()

def insert_players_to_db(players):
    players_table.insert_multiple(players)



if __name__ == '__main__':
    clear_db(players_table)
