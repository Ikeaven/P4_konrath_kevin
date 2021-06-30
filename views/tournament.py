""" Tournament view """

from config import DEFAULT_TOUR_NUMBER, DEFAULT_PLAYERS_NUMBER, TIME_CONTROLLER

from .utilities import UtilitiesView
from .fields import Fields


class TournamentView:

    def __init__(self):
        self.utilities = UtilitiesView()
        self.fields = Fields()

    def get_tournament_info(self):
        """Ask to user to type the tournament informations

        Returns:
            dict: tournament informations
        """
        tournament_name = self.fields.input_text_field("Nom du tournoi : ")
        location = self.fields.input_text_field("Lieu du tournoi : ")
        start_date = self.fields.input_date_field('Entrez la date de début du tournoi (jj/mm/aaaa): ')
        end_date = self.fields.input_date_field_or_empty('Entrez une date de fin (si vide le tournoi durera 1jour): ')
        if end_date == '':
            end_date = start_date
        time_controller = self.fields.input_time_controler(
            'Controller de temps : '
            f'{", ".join([time for time in TIME_CONTROLLER])} : ')

        description = self.fields.input_text_field("Description du tournois : ")
        message_nombre_tour = f"Nombre de tour (si champ vide, {DEFAULT_TOUR_NUMBER} par défaut) : "
        tour_number = self.fields.input_tour_number(message_nombre_tour)
        message_nombre_joueur = f'Nombre de joueurs du tournoi (si vide, default {DEFAULT_PLAYERS_NUMBER}) : '
        number_of_players = self.fields.input_number_of_players(message_nombre_joueur)
        tournament_infos = {'tournament_name': tournament_name,
                            'location': location,
                            'start_date': start_date,
                            'end_date': end_date,
                            'tour_number': tour_number,
                            'time_controller': time_controller,
                            'number_of_players': number_of_players,
                            'description': description}
        return tournament_infos

    def display_tournament_list(self, tournaments_list):
        """Display all tournament informations from a list

        Args:
            tournaments_list (Liste(tournament_instance)): list of Tournaments instances
        """
        self.utilities.line_separator()
        print()
        print('----- LISTE DES TOURNOIS -----')
        print()
        self.utilities.line_separator()
        for index, tournament in enumerate(tournaments_list):
            print(f'Index du tournoi : [{index}]')
            print(f'Nom : {tournament.tournament_name}')
            print(f'Lieu : {tournament.location}')
            print(f'Date de début du tournoi : {tournament.start_date}')
            print(f'Date de fin du tournoi : {tournament.end_date}')
            print(f'Controller de temps : {TIME_CONTROLLER[tournament.time_controller -1]}')
            print(f'Description : {tournament.description}')
            print(f'Nombre de tour : {len(tournament.round_list)}/{tournament.tour_number}')
            if (tournament.round_list[-1].end_round_datetime == 'Round en cours'):
                print('Ce tournoi est toujours en cours')
            else:
                print('Ce tournoi est terminé !')
            self.utilities.line_separator()

    def update_tournament_name(self, tournament):
        """Ask to user to update the tournament name

        Args:
            tournament (obj): Tournament instance to update

        Returns:
            str: new_tournament_name
        """
        print(f'\nNom avant mise à jour : {tournament.tournament_name}')
        new_tournament_name = self.fields.input_text_field('Nouveau nom du tournoi : ')
        return new_tournament_name

    def update_tournament_description(self, tournament):
        """Ask to user to update the tournament description

        Args:
            tournament (obj): Tournament tnstance to update

        Returns:
            str: new_description
        """
        print(f'\nDescription avant mise à jour : {tournament.description}')
        new_description = self.fields.input_text_field('Nouvelle description du tournoi : ')
        return new_description

    def update_time_controller(self, tournament):
        """Ask to user to update the time controller of a tournament

        Args:
            tournament (obj): Tournament instance to update

        Returns:
            str: new_time_controller
        """
        print(f'\nController avant mise à jour : {tournament.time_controller}')
        new_time_controller = self.fields.input_time_controler(
            'Nouveau controller de temps : '
            f'{", ".join([time for time in TIME_CONTROLLER])} : ')
        return new_time_controller

    def update_tournament_location(self, tournament):
        """Ask to update location of a tournament

        Args:
            tournament (obj): Tournament instance to update

        Returns:
            str: new_location
        """
        print(f'\nLieu du tournoi avant mise à jour : {tournament.location}')
        new_location = self.fields.input_text_field('Nouveau lieu du tournoi : ')
        return new_location

    def update_tournament_start_date(self, tournament):
        """Ask to user to update start date

        Args:
            tournament (obj): Tournament instance to update

        Returns:
            str: new_start_date
        """
        print(f'\nDate de début avant mise à jour : {tournament.start_date}')
        new_start_date = self.fields.input_date_field('Nouvelle date de début de tournoi :')
        return new_start_date

    def update_tournament_end_date(self, tournament):
        """Ask to user to update end date

        Args:
            tournament (obj): Tournament instance to update

        Returns:
            str: new_end_date
        """
        print(f'\nDate de fin de tournoi avant mise à jour : {tournament.end_date}')
        new_end_date = self.fields.input_date_field('Nouvelle date de fin de tournoi :')
        return new_end_date
