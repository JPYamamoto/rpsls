import random
from choices import Choice


class Random:
    def prepare_round(self, _):
        pass

    def likely_next(self):
        return Choice.random_choice()

