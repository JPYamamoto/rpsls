import random


class Choice:

    @staticmethod
    def parse(choice):
        choice_id = None
        choice_lower = choice.lower()

        if choice_lower == 'rock':
            return Rock()
        elif choice_lower == 'paper':
            return Paper()
        elif choice_lower == 'scissors':
            return Scissors()
        elif choice_lower == 'lizard':
            return Lizard()
        elif choice_lower == 'spock':
            return Spock()
        else:
            raise ValueError('Invalid choice')

    @staticmethod
    def random_choice():
        choices = Choice.__subclasses__()
        return random.choice(choices)

    @classmethod
    def is_draw(cls, attacker):
        return isinstance(attacker, cls)

    @classmethod
    def get_attacker(cls):
        next_attacker = random.choice(cls.is_beaten_by)
        return Choice.parse(next_attacker)

    @classmethod
    def __eq__(cls, other):
        return isinstance(other, cls)


class Rock(Choice):

    name = 'rock'
    is_beaten_by = ('paper', 'spock')

    def beats(self, attacker):
        if isinstance(attacker, Scissors):
            return True

        if isinstance(attacker, Lizard):
            return True

        return False

    def __str__(self):
        return self.name


class Paper(Choice):

    name = 'paper'
    is_beaten_by = ('lizard', 'scissors')

    def beats(self, attacker):
        if isinstance(attacker, Rock):
            return True

        if isinstance(attacker, Spock):
            return True

        return False

    def __str__(self):
        return self.name


class Scissors(Choice):

    name = 'scissors'
    is_beaten_by = ('rock', 'spock')

    def beats(self, attacker):
        if isinstance(attacker, Paper):
            return True

        if isinstance(attacker, Lizard):
            return True

        return False

    def __str__(self):
        return self.name


class Lizard(Choice):

    name = 'lizard'
    is_beaten_by = ('rock', 'scissors')

    def beats(self, attacker):
        if isinstance(attacker, Spock):
            return True

        if isinstance(attacker, Paper):
            return True

        return False

    def __str__(self):
        return self.name


class Spock(Choice):

    name = 'spock'
    is_beaten_by = ('lizard', 'paper')

    def beats(self, attacker):
        if isinstance(attacker, Rock):
            return True

        if isinstance(attacker, Scissors):
            return True

        return False

    def __str__(self):
        return self.name

