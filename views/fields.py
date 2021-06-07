import config as config
import utilities.checker as check


class Fields:

    @check.checker_text_field
    def input_text_field(self, prompte):
        return input(prompte)

    @check.date_validation
    def input_date_field(self, prompte):
        return input(prompte)

    @check.sex_validation
    def input_sex_field(self, prompte):
        return input(prompte)

    @check.checker_digit_field
    def input_digit_field(self, prompt):
        return input(prompt)

    # TODO : mettre les valeurs dans les variables de config
    @check.checker_menu(1, 3)
    def input_time_controler(self, prompt):
        return input(prompt)

    @check.checker_digit_or_empy_default_field(config.DEFAULT_TOUR_NUMBER)
    def input_tour_number(self, prompt):
        return input(prompt)

    @check.checker_digit_or_empy_default_field(config.DEFAULT_PLAYERS_NUMBER)
    def input_number_of_players(self, prompt):
        return input(prompt)

    @check.checker_menu(0, 2)
    def input_winner(self, prompt):
        return input(prompt)
