"""Menu View"""


from .utilities import UtilitiesView


class MenuView:

    def __init__(self):
        self.utilities = UtilitiesView()

    def prompt_menu(self):
        print("[1] Créer un nouveau tournois")
        print("[2] Editer un tournois")
        print("[3] Editer un joueur")
        print("[5] Quitter")
        menu_value = input('entrer le numéro du menu :')
        if menu_value not in ('1', '2', '3', '5'):
            return None
        return menu_value
