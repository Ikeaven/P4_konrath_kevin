from views.player import PlayerView
from views.utilities import UtilitiesView
from views.tournament import TournamentView
from views.round import RoundView
from views.score import ScoreView
from views.menu import MenuView

from .sort import sort_list_by


# TODO pourquoi il y a des modèles dans mon controller view ?
from models.tournament import Tournament
from models.player import Player


class ViewsController:

    def __init__(self) -> None:
        self.score = ScoreView()
        self.tournament_view = TournamentView()
        self.menu_view = MenuView()
        self.utilities_view = UtilitiesView()
        self.player_view = PlayerView()

    # Display lists
    def display_match_of_tournament(self):
        """Select the tournament and call the view to display match of a tournament."""
        # TODO : function select item...
        selected_tournament = self.select_tournament()
        RoundView().display_round(selected_tournament, True)

    def display_round_of_tournament(self):
        """Call the view to display round of tournament."""
        # TODO : fucntion select item
        selected_tournament = self.select_tournament()
        RoundView().display_round(selected_tournament)

    def select_tournament(self) -> object:
        """Allow the user to choose the turnament.

        Returns:
            instance of Tournament
        """
        # Selectionner un tournoi -> afficher les tournois
        self.tournament_view.display_tournament_list(Tournament().LISTE_TOURNOIS)
        # choisir l'ordre d'affichage
        number_item = self.menu_view.select_item('tournois')
        if number_item.isdigit():
            selected_tournament = Tournament().LISTE_TOURNOIS[int(number_item)]
            return selected_tournament
        else:
            return None

    def display_players_of_tournament(self):
        """Display players of a tournament."""
        # affiche les tournois - et choix
        selected_tournament = self.select_tournament()
        # afficher les joueurs du tournoi
        players = selected_tournament.players_list
        # Ranger la liste par ordre alphabetique ou par classement
        sort_by = self.menu_view.select_sorting()
        sorted_list = sort_list_by(players, sort_by)
        # afficher les joueurs par ordre souhaité
        self.player_view.display_players_list(sorted_list)

    def display_all_players_from_model(self):
        """Display all players."""
        self.all_players = Player.get_all_players()
        self.player_view.display_players_list(self.all_players)

    def display_match_of_round(self, round):
        """Display all matchs of a round

        Keyword arguments:
        round : Round -- Instance of Round
        """
        for match in round.matchs:
            self.score.display_match(match)

    def get_tournament_info(self) -> dict:
        return self.tournament_view.get_tournament_info()

    def display_error(self):
        self.utilities_view.display_error()
