""" Swiss System

    This system generates pairs of players

"""


class Suisse:
    """Generates matchs of round with Suisse syteme
    """
    # #######################
    # ----- FIRST ROUND -----
    # #######################
    def sort_list_by_ranking(self, players_list):
        """Sort a list of players by ranking.

        Args:
            players_list [Player_instance]: List of players instance

        Returns:
            sorted_list - [Player_instance]: sorted list of player instances, sorted by ranking
        """
        sorted_list = sorted(players_list, key=lambda x: x.ranking, reverse=True)
        return sorted_list

    def split_list(self, sorted_list):
        """Split a list in two list

        Args:
            sorted_list (List): list of player instance

        Returns:
            upper_list, lower_list : two list => each half of sorted_list
        """
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
        """Associates best player of first list to best player to second list.

        Args:
            upper_list (List): List of player
            lower_list (List): List of player

        Returns:
            match_list: list of matchs for the first round
        """
        match_list = []
        if len(upper_list) == len(lower_list):
            for i in range(len(upper_list)):
                match_list.append((upper_list[i], lower_list[i]))

        elif len(upper_list) > len(lower_list):
            for i in range(len(lower_list)):
                match_list.append((upper_list[i], lower_list[i]))
        else:
            for i in range(len(upper_list)):
                match_list.append((upper_list[i], lower_list[i]))
        return match_list

    def generate_first_round(self, players_list):
        """Generate first rounds

        Args:
            players_list (List): list of players instance

        Returns:
            match list: matchs list for the first round
        """
        sorted_list = self.sort_list_by_ranking(players_list)
        upper_list, lower_list = self.split_list(sorted_list)
        matchs_list = self.first_round_player_association(upper_list, lower_list)
        return matchs_list

    # ########################
    # ----- NEXT ROUNDS -----
    # ########################
    def get_players_list_with_score(self, previous_round):
        """Get players and result for the previous round

        Args:
            previous_round (obj): last round that just finished

        Returns:
            players_with_score: [[player, score_player], [player, score_player], [player, score_player], ...]
        """
        players_with_score = []
        for match in previous_round.matchs:
            player1 = [match.player1, match.score_player1]
            players_with_score.append(player1)

            player2 = [match.player2, match.score_player2]
            players_with_score.append(player2)
        return players_with_score

    def sort_list_by_score(self, players_list_with_score):
        """Sort players by score and by ranking.

        Args:
            players_list_with_score (List): list of players with score:
                [[player, score], [player, score], ...]

        Returns:
            List: sorted_list_by_score, if multiple players have the same score,
                    they are sorted by ranking
        """
        sorted_list_by_ranking = sorted(players_list_with_score, key=lambda x: x[0].ranking, reverse=True)
        sorted_list_by_score = sorted(sorted_list_by_ranking, key=lambda x: x[1], reverse=True)
        return sorted_list_by_score

    def check_association(self, player1, player2, tournament):
        """Check if player1 already played against player2.

        Args:
            player1 (Player instance): a player instance
            player2 (Player instance): a player instance
            tournament (Tournament instance): check inside this tournament

        Returns:
            Boolean :
                if player1 already played against player2 retrun False.
                else retrun True.
        """
        for round in tournament.round_list:
            for match in round.matchs:
                if (player1 == match.player1 or player1 == match.player2) and (
                    player2 == match.player1 or player2 == match.player2
                ):
                    return False
        return True

    def next_round_player_association(self, players_list_with_score, tournament):
        """Associates players by score for the next round

        Args:
            players_list_with_score (List):
                list of player, with score, sorted by score and ranking
                [[player1, score1], [player2, score2], ...]

            tournament (tournament instance): tournament instance

        Yields:
            tuple: ([player1, score_player1], [player2, score_player2])
        """
        associated_players = []
        for i, player in enumerate(players_list_with_score):
            # if we already associate this player just jump to next player
            if player[0] in associated_players:
                continue
            # else we can associate it to the other one
            else:
                next_player = i+1
                while True:
                    try:
                        # If second player already associated, just jump to next player
                        while players_list_with_score[next_player][0] in associated_players:
                            next_player += 1
                        # If this association has not yet taken place in this tournament, we have our match !!
                        if self.check_association(player[0], players_list_with_score[next_player][0], tournament):
                            associated_players.append(player[0])
                            associated_players.append(players_list_with_score[next_player][0])
                            yield (player, players_list_with_score[next_player])
                            break
                        # Else, try with next player
                        else:
                            next_player += 1
                    except IndexError:
                        print('Tournois terminé !')
                        break

    def generate_next_round(self, previous_round, tournament):
        """Create match_list for the next round.

        Args:
            previous_round (Round instance): last round, that just finished
            tournament (Tournament instance): tournament.

        Returns:
            List:
                list of matchs, for the next round
                [([player1, score_player1], [player2, score_player2]), ([player1, score_player1],...)]
        """
        players_list_with_score = self.get_players_list_with_score(previous_round)
        sorted_list = self.sort_list_by_score(players_list_with_score)
        match_list = []
        for match in self.next_round_player_association(sorted_list, tournament):
            match_list.append(match)
        return match_list
