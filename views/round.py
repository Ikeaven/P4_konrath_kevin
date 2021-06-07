""" Round View """


from .fields import Fields

class RoundView:
    def dispalay_start_time(self):
        pass

    def display_stop_time(self, round):
        print(f'Arrêt à : {round.end_round_datetime}')

    def start_new_round(self):
        print("Un nouveau round a été généré automatiquement, le tournoi n'est pas terminé !!")
        print("Voici les matchs suivant : ")
