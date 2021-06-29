""" Fields Modul

    Every fields has a checker with a decorators
"""

from config import TIME_CONTROLLER, DEFAULT_TOUR_NUMBER, DEFAULT_PLAYERS_NUMBER
import utilities.checker as check


class Fields:

    @check.checker_text_field
    def input_text_field(self, message):
        return input(message)

    @check.date_validation
    def input_date_field(self, message):
        return input(message)

    @check.date_validation_or_empty
    def input_date_field_or_empty(self, message):
        return input(message)

    @check.sex_validation
    def input_sex_field(self, message):
        return input(message)

    @check.checker_digit_field
    def input_digit_field(self, message):
        return input(message)

    @check.checker_menu(1, len(TIME_CONTROLLER))
    def input_time_controler(self, message):
        return input(message)

    @check.checker_digit_or_empy_default_field(DEFAULT_TOUR_NUMBER)
    def input_tour_number(self, message):
        return input(message)

    @check.checker_digit_or_empy_default_field(DEFAULT_PLAYERS_NUMBER)
    def input_number_of_players(self, message):
        return input(message)

    @check.checker_menu(0, 2)
    def input_winner(self, message):
        return input(message)
