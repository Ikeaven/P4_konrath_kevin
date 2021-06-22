from .view import ViewsController
from .models import ModelsController
from .db import DBController

from models.player import Player
from models.tournament import Tournament

from views.utilities import UtilitiesView
from views.player import PlayerView
from views.menu import MenuView
from views.tournament import TournamentView


class Router:

    def __init__(self) -> None:
        self.model_controller = ModelsController()
        self.view_controller = ViewsController()
        self.db_controller = DBController()

        self.player_view = PlayerView()
        self.menu_view = MenuView()
        self.tournament_view = TournamentView()
        self.utilities_view = UtilitiesView()

    def main_menu(self, selected_menu):
        """Cette fonction déclenche des méthodes en fonction du choix de l'utilisateur."""
        # Create new tournament
        if selected_menu == '1':
            self.model_controller.create_tournament()

        # Edit tournament
        elif selected_menu == '2':
            selected_tournament = self.view_controller.select_tournament()
            if selected_tournament:
                self.edit_tournament_menu(selected_tournament)
            else:
                return True

        # Edit player
        elif selected_menu == '3':
            if Player.get_all_players() is not None:
                self.player_view.display_players_list(Player.get_all_players())
                player_id: int = int(self.menu_view.select_item('joueur'))
                if player_id == 'X':
                    pass
                else:
                    selected_player: object = Player.get_all_players()[player_id]
                    self.edit_player_menu(selected_player)

        # Rapports
        elif selected_menu == '4':
            self.reports_menu()

        # Load data from database
        elif selected_menu == '5':
            self.db_controller.load_players()
            self.db_controller.load_tournaments()

        # Save
        elif selected_menu == '7':
            self.db_controller.save_to_tinydb(Player().LIST_PLAYERS, Tournament().LISTE_TOURNOIS)

        # TEST generate tournament auto
        elif selected_menu == '8':
            self.model_controller.TEST_import_auto_tournoi()

        # stop
        elif selected_menu == '9':
            return False

        # error : value not found
        else:
            self.utilities_view.display_error()

    def edit_tournament_menu(self, tournament: object):
        selected_menu = self.menu_view.display_menu_edit_tournament(tournament)
        # end of the round -> update score
        if selected_menu == '1':
            self.model_controller.end_of_round(tournament)
        # change name of tournament
        elif selected_menu == '2':
            new_tournament_name = self.tournament_view.update_tournament_name(tournament)
            tournament.update_name(new_tournament_name)
        # change description
        elif selected_menu == '3':
            new_description = self.tournament_view.update_tournament_description(tournament)
            tournament.update_description(new_description)
        # change time controller
        elif selected_menu == '4':
            new_time_controller = self.tournament_view.update_time_controller(tournament)
            tournament.update_time_controller(new_time_controller)
        # change tournament's location
        elif selected_menu == '5':
            new_location = self.tournament_view.update_tournament_location(tournament)
            tournament.update_location(new_location)
        # return to main menu
        elif selected_menu == '6':
            self.main_menu()
        # error : value not found
        else:
            self.utilities_view.display_error()

    def edit_player_menu(self, player: object):
        selected_menu = self.menu_view.display_menu_edit_player()
        # Editer the ranking
        if selected_menu == '1':
            new_ranking = self.player_view.update_ranking(player)
            player.update_ranking(new_ranking)

        # Edit first name and last name
        elif selected_menu == '2':
            new_first_name, new_last_name = self.player_view.update_name(player)
            player.update_name(new_first_name, new_last_name)
        # Edit date of birth
        elif selected_menu == '3':
            new_date_of_birth = self.player_view.update_birthday(player)
            player.update_birthday(new_date_of_birth)
        #  Edit sex
        elif selected_menu == '4':
            new_sex = self.player_view.update_sex(player)
            player.update_sex(new_sex)
        # Return to main menu
        elif selected_menu == '5':
            pass
        else:
            self.utilities_view.display_error()

    def reports_menu(self):
        """Choice - Menu reports."""
        selected_menu = self.menu_view.display_report_menu()

        # Afficher tous les joueurs
        if selected_menu == '1':
            # TODO demande dans quel tri -> Alpha / Classement
            players = Player.LIST_PLAYERS
            self.player_view.display_players_list(players)

        # Afficher les joueurs d'un tournois
        elif selected_menu == '2':
            self.view_controller.display_players_of_tournament()

        # Afficher les tournois
        elif selected_menu == '3':
            self.tournament_view.display_tournament_list(Tournament.LISTE_TOURNOIS)

        # Afficher les rounds d'un tournoi
        elif selected_menu == '4':
            self.view_controller.display_round_of_tournament()

        # Liste des matchs d'un tournoi
        elif selected_menu == '5':
            self.view_controller.display_match_of_tournament()

        # retour au menu principal
        elif selected_menu == '6':
            pass

        # Le choix n'est pas dans les propositions du menu
        else:
            UtilitiesView().display_error()
