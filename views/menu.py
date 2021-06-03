"""Menu View"""


from .utilities import UtilitiesView


class MenuView:

    def __init__(self):
        self.utilities = UtilitiesView()

    def prompt_menu(self):
        print("[1] Créer un nouveau tournoi")
        print("[2] Editer un tournoi")
        print("[3] Editer un joueur")
        print('[4] Afficher les joueurs')
        print('[5] Afficher les tournois')
        print("[9] Quitter")
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def prompt_menu_edition_joueur(self):
        print('[1] Afficher tous les joueurs')
        print('[2] modifier un joueur')

    def prompt_menu_add_player(self):
        print('[1] Ajouter joueur a partir des joueurs déjà enregistré')
        print('[2] Ajouter un nouveau joueur')
        menu_value = input('entrer le numéro du menu :')
        return menu_value