import random
from choices import Choice


class MarkovChainMixin:

    matrix = {
        'rock':     {'rock': 0, 'paper': 0, 'scissors': 0, 'lizard': 0, 'spock': 0},
        'paper':    {'rock': 0, 'paper': 0, 'scissors': 0, 'lizard': 0, 'spock': 0},
        'scissors': {'rock': 0, 'paper': 0, 'scissors': 0, 'lizard': 0, 'spock': 0},
        'lizard':   {'rock': 0, 'paper': 0, 'scissors': 0, 'lizard': 0, 'spock': 0},
        'spock':    {'rock': 0, 'paper': 0, 'scissors': 0, 'lizard': 0, 'spock': 0}
    }

    prev_throw = None
    last_throw = None

    def prepare_round(self, throw):
        self.prev_throw = self.last_throw
        self.last_throw = throw

        if self.prev_throw is not None:
            self.matrix[str(self.prev_throw)][str(self.last_throw)] += 1

    def likely_next(self):
        if self.last_throw is None:
            return Choice.random_choice()

        return self.implementation()


class MarkovChain(MarkovChainMixin):
    def implementation(self):
        matrix = self.matrix[str(self.last_throw)]
        max_times = matrix[max(matrix, key=lambda val: matrix[val])]
        next_options = [k for (k,v) in matrix.items() if v == max_times]
        next_str = random.choice(next_options)
        return Choice.parse(next_str)


class RandomMarkovChain(MarkovChainMixin):
    def implementation(self):
        matrix = self.matrix[str(self.last_throw)]
        options, weights = zip(*matrix.items())
        next_str = random.choices(options, weights=weights)[0]
        return Choice.parse(next_str)

