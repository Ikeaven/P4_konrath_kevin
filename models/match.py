""" Match model """


from uuid import uuid1


class Match:

    def create_match(self, player1, score_player1, player2, score_player2):
        self.id = str(uuid1())
        self.player1 = player1
        self.score_player1 = score_player1

        self.player2 = player2
        self.score_player2 = score_player2
        return self
