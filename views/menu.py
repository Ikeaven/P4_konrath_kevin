"""Menu View"""


from .utilities import UtilitiesView
# TODO UTILISER LES FIELDS avec vérif !!


class MenuView:

    def __init__(self):
        self.utilities = UtilitiesView()

    def display_menu(self):
        print()
        print("----- MENU PRINCIPAL -----")
        print()
        print("[1] Créer un nouveau tournoi")
        print("[2] Editer un tournoi")
        print("[3] Editer un joueur")
        print('[4] Rapports')
        # print('[5] Afficher les tournois')
        print('[6] Fin de round')
        print('[8] Générer tournois automatiquement')
        print("[9] Quitter")
        print()
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def display_menu_edition_joueur(self):
        print('[1] Afficher tous les joueurs')
        print('[2] modifier un joueur')

    def display_menu_add_player(self):
        print('[1] Ajouter joueur a partir des joueurs déjà enregistrés')
        print('[2] Ajouter un nouveau joueur')
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def test_import_auto(self):
        print('[1] INSERT PLAYERS AUTO')
        print('[2] INSERT PLAYERS MANUEL')
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def select_item(self):
        menu_value = input("selectionner l'item avec l'index : ")
        return menu_value

    def display_report_menu(self):
        print()
        print("----- MENU RAPPORTS -----")
        print()
        print('[1] Liste des acteurs')
        print("[2] Liste des joueurs d'un tournoi")
        print("[3] Liste des tournois")
        print("[4] Liste des tours d'un tournoi")
        print("[5] Liste des matchs d'un tournoi")
        print("[6] Retour au menu principal")
        print()
        menu_value = input("entrer le numéro du menu : ")
        return menu_value

    def select_sorting(self):
        print("[1] Ordre alphabétique")
        print("[2] Ordre de classement")
        menu_value = input("selectionner un ordre de tri : ")
        return menu_value


