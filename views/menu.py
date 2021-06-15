"""Menu View"""


from .utilities import UtilitiesView
# TODO UTILISER LES FIELDS avec vérif !!
# TODO decorateur 'entrez le numéro du menu... 

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
        print('[5] Chargement de la base de donnée')
       
        # print('[6] Fin de round')
        print('[7] Sauvegarder')
        print('[8] Générer tournois automatiquement')
        print("[9] Quitter")
        print()
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def display_menu_edit_player(self):
        print()
        print("----- MENU EDITION D'UN JOUEUR -----")
        print()
        print('[1] Editer classement')
        print('[2] Editer Nom et Prénom')
        print("[3] Editer date d'anniversaire ")
        print('[4] Editer sexe du joueur')
        print('[5] Retour au menu principal')
        menu_value = input('entrer le numéro du menu :')
        return menu_value


    def display_menu_add_player(self):
        print('[1] Ajouter joueur a partir des joueurs déjà enregistrés')
        print('[2] Ajouter un nouveau joueur')
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def display_menu_edit_tournament(self, tournament):
        print()
        print("----- MENU EDITION DU TOURNOI -----")
        print()
        
        if tournament.round_list[-1].end_round_datetime == 'Round en cours':
            print('[1] Fin du round : mise à jour des scores')
        print('[2] Changer le nom')
        print('[3] Changer la description')
        print('[4] Changer le controller de temps')
        print('[5] Retour au menu principal')
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def test_import_auto(self):
        print('[1] INSERT PLAYERS AUTO')
        print('[2] INSERT PLAYERS MANUEL')
        menu_value = input('entrer le numéro du menu :')
        return menu_value

    def select_item(self, item):
        if item in ['joueur', 'tournois'] :
            determinant = 'le'
        else:
            determinant = 'la'
        menu_value = input(f"selectionner {determinant} {item} avec l'index : ")
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


