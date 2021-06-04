from .fields import Fields

class RoundView:
    def dispalay_start_time(self):
        pass

    def display_stop_time(self, round):
        print(f'Arrêt à : {round.end_round_datetime}')

    def start_new_round(self):
        print("Un nouveau round va être généré automatiquement si le tournoi n'est pas terminé")
