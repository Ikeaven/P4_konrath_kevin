""" Match model """


from uuid import uuid1


class Match:

    def create_match(self, player1, score_player1, player2, score_player2) -> object:
        self.id = str(uuid1())
        self.player1 = player1
        self.score_player1 = score_player1

        self.player2 = player2
        self.score_player2 = score_player2
        return self

    def load_match(self, match_info: dict) -> object:
        self.id = match_info['id']
        self.player1 = match_info['player1']
        self.score_player1 = match_info['score_player1']
        self.player2 = match_info['player2']
        self.score_player2 = match_info['score_player2']
        return self
