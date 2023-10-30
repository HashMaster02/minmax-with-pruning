
class AI:

    def __init__(self):
        self.utility = {'X': 1, 'O': -1, 'TIE': 0}

    def min_max(self, game):
        # is_winner = game.has_ended(game.current_player)
        if game.has_ended(game.current_player):
            return None, self.calculate_utility(game.current_player, game.board.available_moves)

        # Max-player
        if game.current_player == "X":
            (move, value) = (None, -10000)
            for action in game.board.available_moves:
                game.play_move(action)
                game.next_player()
                (_, new_value) = self.min_max(game)
                game.undo_move(action)

                if new_value > value:
                    (move, value) = (action, new_value)

            return move, value

        # Min-player
        if game.current_player == "O":
            (move, value) = (None, 10000)
            for action in game.board.available_moves:
                game.play_move(action)
                game.next_player()
                (_, new_value) = self.min_max(game)
                game.undo_move(action)

                if new_value < value:
                    (move, value) = (action, new_value)

            return move, value

    def calculate_utility(self, player, remaining_moves):
        constant = self.utility[player]
        return constant * (len(remaining_moves) + 2)
