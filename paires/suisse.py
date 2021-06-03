""" Système Suisse 
    1. trie tous les joueurs en fonction du classement
    2. Divise les joueurs en 2 moitiers (supérieurs / inférieur)
    3. Le meilleur de la moitier supérieur est jumelé avec le meilleur de la moitier inférieur
    4. Trier maitenant les joueurs en fonction de leur nombre de points 
    5. Associer joueur 1 avec joueur 2, joueur 3 avec 4... Si le joueur 1 à déjà joué contre 2 alors l'associer avec 3... 
    6. répéter les étapes 4 et 5
"""

class Suisse:

    def sort_list(self, players_list):
        sorted_list = sorted(players_list, key=lambda x: x.ranking, reverse=True)
        for el in sorted_list:
            print(el.first_name)
        return sorted_list

    def split_list(self, sorted_list):
        length = len(sorted_list)/2
        upper_list = []
        lower_list = []
        for i, player in enumerate(sorted_list):
            if i < length:
                upper_list.append(player)
            else:
                lower_list.append(player)   
        return upper_list, lower_list

    def first_round_player_association(self, upper_list, lower_list):
        round_list = []
        if len(upper_list) == len(lower_list):
            for i in range(len(upper_list)):
                round_list.append(([upper_list[i], 0], [lower_list[i], 0]))

        elif len(upper_list) > len(lower_list):
            for i in range(len(lower_list)):
                round_list.append(([upper_list[i], 0], [lower_list[i], 0]))
        else:
            for i in range(len(upper_list)):
                round_list.append(([upper_list[i], 0], [lower_list[i], 0]))
            
        return round_list


    def generate_round(self, players_list):
        sorted_list = self.sort_list(players_list) 
        upper_list, lower_list = self.split_list(sorted_list)
        round_list = self.first_round_player_association(upper_list, lower_list)
        print(round_list)