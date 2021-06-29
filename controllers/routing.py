""" ROUTING """



from paires.suisse import Suisse
from .view import ViewsController
from .models import ModelsController
from .db import DBController

from models.player import Player
from models.tournament import Tournament

from views.utilities import UtilitiesView
from views.player import PlayerView
from views.menu import MenuView
from views.tournament import TournamentView
from views.score import ScoreView


class Router:

    def __init__(self) -> None:
        self.model_controller = ModelsController()
        self.view_controller = ViewsController()
        self.db_controller = DBController()

        self.player_view = PlayerView()
        self.menu_view = MenuView()
        self.tournament_view = TournamentView()
        self.utilities_view = UtilitiesView()
        self.score_view = ScoreView()

    def main_menu(self, selected_menu):
        """Main Menu:
            - 1 : Create tournament
            - 2 : Create new player
            - 3 : Edit tournament
            - 4 : Edit player
            - 5 : Rapports
            - 6 : Load data from database
            - 7 : Save to database
            - 8 : DEMO generate auto tournament
            - 9 : Stop

        Args:
            selected_menu (str): input user

        Returns:
            False : to Stop the loop with [9]
        """
        # Create new tournament
        if selected_menu == '1':
            self.model_controller.create_tournament()

        # Create new player
        if selected_menu == '2':
            player_info = self.model_controller.ask_player_info(len(Player.LIST_PLAYERS))
            self.model_controller.create_new_player(player_info)

        # Edit tournament
        elif selected_menu == '3':
            if len(Tournament.TOURNAMENT_LIST) >= 1:
                selected_tournament = self.view_controller.select_tournament()
                if selected_tournament:
                    self.edit_tournament_menu(selected_tournament)
                else:
                    pass
            else:
                self.utilities_view.display_error_with_message('Pas de tournois enregistré pour le moment !')

        # Edit player
        elif selected_menu == '4':
            if Player.get_all_players() is not None:
                self.player_view.display_players_list(Player.get_all_players())
                player_id: int = int(self.menu_view.select_item('joueur'))
                if player_id == 'X':
                    pass
                else:
                    selected_player: object = Player.get_all_players()[player_id]
                    self.edit_player_menu(selected_player)

        # Rapports
        elif selected_menu == '5':
            self.reports_menu()

        # Load data from database
        elif selected_menu == '6':
            self.db_controller.load_players()
            self.db_controller.load_tournaments()

        # Save
        elif selected_menu == '7':
            self.db_controller.save_to_tinydb(Player().LIST_PLAYERS, Tournament().TOURNAMENT_LIST)

        # DEMO generate tournament auto
        elif selected_menu == '8':
            self.model_controller.DEMO_import_auto_tournament()

        # stop
        elif selected_menu == '9':
            return False

    def edit_tournament_menu(self, tournament: object):
        """Tournament edition menu
            1 : End of a round
            2 : Change Name
            3 : Change Description
            4 : Change time controller
            5 : Change Location
            6 : Change Sart date
            7 : Change End Date
            8 : Return to main menu
        Args:
            tournament (object): Instance of tournament, we want to edit.
        """
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
        # change start_date
        elif selected_menu == '6':
            new_start_date = self.tournament_view.update_tournament_start_date(tournament)
            tournament.update_start_date(new_start_date)
        # change end_date
        elif selected_menu == '7':
            new_end_date = self.tournament_view.update_tournament_end_date(tournament)
            tournament.update_end_date(new_end_date)
        # return to main menu
        elif selected_menu == '8':
            pass
        # error : value not found
        else:
            self.utilities_view.display_error()

    def edit_player_menu(self, player: object):
        """Menu player edition

        Args:
            player (object): Player instance we want to edit
        """
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
            if len(Player.LIST_PLAYERS) >= 1:
                self.view_controller.display_all_players_sorted()
            else:
                self.utilities_view.display_error_with_message('Pas de joueur enregistré pour le moment !')

        # Afficher les joueurs d'un tournois
        elif selected_menu == '2':
            if len(Tournament.TOURNAMENT_LIST) >= 1:
                self.view_controller.display_players_of_tournament()
            else:
                self.utilities_view.display_error_with_message('Pas de tournois enregistré pour le moment !')

        # Afficher les tournois
        elif selected_menu == '3':
            if len(Tournament.TOURNAMENT_LIST) >= 1:
                self.tournament_view.display_tournament_list(Tournament.TOURNAMENT_LIST)
            else:
                self.utilities_view.display_error_with_message('Pas de tournois enregistré pour le moment !')

        # Afficher les rounds d'un tournoi
        elif selected_menu == '4':
            if len(Tournament.TOURNAMENT_LIST) >= 1:
                self.view_controller.display_round_of_tournament()
            else:
                self.utilities_view.display_error_with_message('Pas de tournois enregistré pour le moment !')

        # Liste des matchs d'un tournoi
        elif selected_menu == '5':
            if len(Tournament.TOURNAMENT_LIST) >= 1:
                self.view_controller.display_match_of_tournament()
            else:
                self.utilities_view.display_error_with_message('Pas de tournois enregistré pour le moment !')

        elif selected_menu == '6':
            ended_tournaments = self.model_controller.get_ended_tournament()
            self.tournament_view.display_tournament_list(ended_tournaments)
            selected_tournoi = ended_tournaments[int(self.menu_view.select_item('tournoi'))]
            player_with_score = Suisse().get_players_list_with_score(selected_tournoi.round_list[-1])
            sorted_player_list = Suisse().sort_list_by_score(player_with_score)
            self.score_view.display_final_score(sorted_player_list)

        # retour au menu principal
        elif selected_menu == '7':
            pass

        # Le choix n'est pas dans les propositions du menu
        else:
            UtilitiesView().display_error()
