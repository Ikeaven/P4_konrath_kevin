""" Variables de configuration """

# TIME IN LOCAL LANGUAGE
import locale
locale.setlocale(locale.LC_TIME, "fr_FR")

# TIME CONTROLLER LIST
TIME_CONTROLLER = ['[1] Bullet', '[2] Blitz', '[3] Coup rapide']

# DEFAULTS VARIABLES
DEFAULT_TOUR_NUMBER = 4
DEFAULT_PLAYERS_NUMBER = 8

# Update score
SCORE_FOR_WINNER = 1
SCORE_FOR_NULL = 0.5

# DB NAME
DB_NAME = 'db.json'
