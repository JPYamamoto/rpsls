import random
from choices import Choice


class Henny:

    last_moves = []

    def prepare_round(self, throw):
        self.last_moves.append(throw)

    def likely_next(self):
        if len(self.last_moves) == 0:
            return Choice.random_choice()

        return random.choice(self.last_moves)

