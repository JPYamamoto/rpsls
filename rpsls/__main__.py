from game import Game
from algorithms.markov import MarkovChain, RandomMarkovChain
from algorithms.random import Random
from algorithms.henny import Henny
from algorithms.hawking import Hawking

if __name__ == '__main__':
    game = Game(Hawking())
    game.play()
    print('-----')
    print('Results')
    print('Win: {} games'.format(game.times_win))
    print('Draw: {} games'.format(game.times_draw))
    print('Lose: {} games'.format(game.times_lose))
    print('-----')
    print('Nice game!')

