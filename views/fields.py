import config_chess_tournament as config
from utilities.checker import checker_digit_field, date_validation, sex_validation, checker_digit_field, checker_text_field
from utilities.checker import checker_menu, checker_digit_or_empy_default_field

class Fields:

    @checker_text_field
    def input_text_field(self, prompte):
        return input(prompte)

    @date_validation
    def input_date_field(self, prompte):
        return input(prompte)

    @sex_validation
    def input_sex_field(self, prompte):
        return input(prompte)

    @checker_digit_field
    def input_digit_field(self, prompt):
        return input(prompt)

    # TODO : mettre les valeurs dans les variables de config
    @checker_menu(1, 3)
    def input_time_controler(self, prompt):
        return input(prompt)

    @checker_digit_or_empy_default_field(config.DEFAULT_TOUR_NUMBER)
    def input_tour_number(self, prompt):
        return input(prompt)

    @checker_digit_or_empy_default_field(config.DEFAULT_PLAYERS_NUMBER)
    def input_number_of_players(self, prompt):
        return input(prompt)