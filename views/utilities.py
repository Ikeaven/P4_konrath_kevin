"""Utilities View"""


class UtilitiesView:
    def line_separator(self):
        print("___________________________________________________________________________________________________________________________")

    def prompt_error_NaN(self):
        self.line_separator()
        print("Erreur. Ce champ n'accepte que les nombres!")
        self.line_separator()

    def prompt_error(self):
        self.line_separator()
        print('Erreur, veuillez rensigner une valeur attendue !')
        self.line_separator()

    def prompt_error_null(self):
        print("Erreur. Ce champ ne peut pas être vide.")
