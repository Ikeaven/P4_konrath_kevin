"""Utilities View"""


class UtilitiesView:
    def line_separator(self):
        """Display a line of 115 underscores."""                
        for _ in range(115):
            print('_', end='')
        print()

    def display_error_NaN(self):
        """Display an error : this field accepts only numbers."""        
        self.line_separator()
        print("Erreur. Ce champ n'accepte que les nombres!")
        self.line_separator()

    def display_error(self):
        """Display a generic error like : value not found."""        
        self.line_separator()
        print('Erreur, valeur non trouvée !')
        self.line_separator()

    def display_error_null(self):
        """Display an error : This field can not be empty"""        
        print("Erreur. Ce champ ne peut pas être vide.")

    def display_tournament_is_finished(self):
        """tournament is finished message"""
        print('Error : Le tournoi est déjà terminé')