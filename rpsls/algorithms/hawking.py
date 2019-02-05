import random
from choices import Choice


class Hawking:

    last_moves = []
    prev_throw = None
    last_throw = None


    def prepare_round(self, throw):
        self.prev_throw = self.last_throw
        self.last_throw = throw

        if self.prev_throw is not None:
            self.last_moves.append((self.prev_throw, self.last_throw))
            self.last_moves = self.last_moves[-20:]

    def likely_next(self):
        if self.last_throw is None:
            return Choice.random_choice()

        filtered = [str(v) for (k,v) in self.last_moves if k == self.last_throw]

        if len(filtered) == 0:
            return Choice.random_choice()

        counter = {}

        for item in filtered:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1

        max_times = counter[max(counter, key=lambda val: counter[val])]
        next_options = [k for (k,v) in counter.items() if v == max_times]
        next_str = random.choice(next_options)

        return Choice.parse(next_str)

