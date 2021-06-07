""" Système Suisse 
    1. trie tous les joueurs en fonction du classement
    2. Divise les joueurs en 2 moitiers (supérieurs / inférieur)
    3. Le meilleur de la moitier supérieur est jumelé avec le meilleur de la moitier inférieur
    4. Trier maitenant les joueurs en fonction de leur nombre de points 
    5. Associer joueur 1 avec joueur 2, joueur 3 avec 4... Si le joueur 1 à déjà joué contre 2 alors l'associer avec 3... 
    6. répéter les étapes 4 et 5
"""

from operator import itemgetter, attrgetter

class Suisse:

    def sort_list(self, players_list):
        sorted_list = sorted(players_list, key=lambda x: x.ranking, reverse=True)
        # for el in sorted_list:
        #     print(el.first_name)
        return sorted_list

    def split_list(self, sorted_list):
        length = len(sorted_list)//2
        upper_list = []
        lower_list = []
        for i, player in enumerate(sorted_list):
            if i < length:
                upper_list.append(player)
            else:
                lower_list.append(player)   
        return upper_list, lower_list

    def first_round_player_association(self, upper_list, lower_list):
        match_list = []
        if len(upper_list) == len(lower_list):
            for i in range(len(upper_list)):
                match_list.append((upper_list[i],lower_list[i]))

        elif len(upper_list) > len(lower_list):
            for i in range(len(lower_list)):
                match_list.append((upper_list[i],lower_list[i]))
        else:
            for i in range(len(upper_list)):
                match_list.append((upper_list[i],lower_list[i]))
        return match_list

   
    def generate_first_round(self, players_list):
        sorted_list = self.sort_list(players_list) 
        upper_list, lower_list = self.split_list(sorted_list)
        round_list = self.first_round_player_association(upper_list, lower_list)
        return round_list


    def get_players_list_with_score(self, previous_round):
        players_with_score = []
        for match in previous_round.matchs:
            player1 = [match.player1, match.score_player1]
            players_with_score.append(player1)

            player2 = [match.player2, match.score_player2]
            players_with_score.append(player2)
        return players_with_score

    def sort_list_by_score(self, players_list_with_score):
        sorted_list_by_ranking = sorted(players_list_with_score, key=lambda x: x[0].ranking, reverse=True)
        sorted_list_by_score = sorted(sorted_list_by_ranking, key=lambda x: x[1], reverse=True)
        return sorted_list_by_score
    
    def check_association(self, player1, player2, tournament):
        for round in tournament.round_list:
            for match in round.matchs:
                if (player1 == match.player1 or player1 == match.player2) and (player2 == match.player1 or player2 == match.player2):
                    return False
        return True
         

    def next_round_player_association(self, players_list_with_score, tournament):
        # TODO : faire de plus petites fonctions 
        # prendre l'utilisateur un et l'associer au second
        # Si l'association a déjà été faite, essayer avec le suivant
        associated_players = []
        # On parcours tous les joueurs
        for i, player in enumerate(players_list_with_score):
            # S'il est déjà associé, on passe au suivant sans rien faire
            if player[0] in associated_players:
                continue
            # Sinon on check si l'association n'a pas déjà eu lieu
            else :
                # TODO si i = len(nombre_de_player... on est au bout)
                next_player = i+1
                while True:
                    try: 
                        # on vérifie si le joueur 2 n'est pas déjà asocié, s'il est associé on passe au suivant
                        while players_list_with_score[next_player][0] in associated_players:
                            next_player += 1
                        # On vérifie les matchs précédent, Si les deux joueurs n'ont pas encore été associé, on créer le match et on met de coté ces utilisateurs
                        if self.check_association(player[0], players_list_with_score[next_player][0], tournament):
                            associated_players.append(player[0])
                            associated_players.append(players_list_with_score[next_player][0])
                            yield (player, players_list_with_score[next_player])
                            break
                        # Sinon on cherche avec l'utilisateur suivant
                        else:
                            next_player += 1
                    except IndexError:
                        print('Tournois terminé !')
                        break



    def generate_next_round(self, previous_round, tournament):
        # récupère la liste des joueurs avec le score du tournois
        players_list_with_score = self.get_players_list_with_score(previous_round)
        # trie la liste en fonction du ranking, puis du score
        sorted_list = self.sort_list_by_score(players_list_with_score)
        # association des joueurs
        match_list = []
        for match in self.next_round_player_association(sorted_list, tournament):
            match_list.append(match)
        return match_list