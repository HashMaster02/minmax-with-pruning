from random import randint


class AI:

    def __init__(self):
        self.utility = {'X': 1, 'O': -1, 'TIE': 0}

    def random_spot(self, moves):
        return moves[randint(0, len(moves)-1)]

    def min_max(self, game, board):
        pass

    def min_max_pruning(self, game, board):
        pass
