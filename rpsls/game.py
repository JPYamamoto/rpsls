from choices import Choice


class Game:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.times_win = 0
        self.times_draw = 0
        self.times_lose = 0

    def round_result(self, user, computer):
        if user.beats(computer):
            self.times_win += 1
            return 'WIN'
        elif user.is_draw(computer):
            self.times_draw += 1
            return 'DRAW'
        else:
            self.times_lose += 1
            return 'LOSE'

    def print_result(self, user, computer, result):
        print('----------')
        print('You: {}'.format(user))
        print('Computer: {}'.format(computer))

        if result == 'WIN':
            print('You win')
        elif result == 'DRAW':
            print('It\'s a draw')
        else:
            print('Computer wins')

        print('----------')

    def play(self):
        while True:
            computer = self.algorithm.likely_next().get_attacker()

            user_in = input('What do you want to throw?: ').lower()

            if user_in == 'exit':
                break

            try:
                user = Choice.parse(user_in)
                self.algorithm.prepare_round(user)
                result = self.round_result(user, computer)
                self.print_result(user, computer, result)
            except ValueError as e:
                print('Wrong input. Try again.')

