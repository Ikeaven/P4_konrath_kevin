""" Round model """ 

class Round:
    
    def create_round(self, round_name):
        self.round_name = round_name
        self.matchs = []
        return self

    def add_match_to_round(self, match):
        self.matchs.append(match)
