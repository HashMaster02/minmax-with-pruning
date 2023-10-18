
class Board:

    def __init__(self):
        self.game_board = [[' ', ' ', ' '],
                           [' ', ' ', ' '],
                           [' ', ' ', ' ']]
        self.available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.winning_cells = [(1,2,3), (4,5,6), (7,8,9),
                              (1,4,7), (2,5,8), (3,6,9),
                              (1,5,9), (3,5,7)]

    def make_move(self, position: int, player: str):

        try:
            self.available_moves.index(position)
            self.game_board[(position - 1) // 3][(position % 3) - 1] = player
            self.available_moves.remove(position)
            return True
        except ValueError:
            print("___________________________________")
            print("Illegal move. Try again.")
            return False

    def check_win_conditions(self):
        for (x, y, z) in self.winning_cells:
            if self.get_position(x) == self.get_position(y) == self.get_position(z) == 'X' or self.get_position(x) == self.get_position(y) == self.get_position(z) == 'O':
                print("___________________________________")
                self.print_board()
                return self.get_position(x)

        if len(self.available_moves) == 0:
            return 'Draw'

        return ''

    def get_position(self, position):
        return self.game_board[(position - 1) // 3][(position % 3) - 1]

    def print_board(self):
        for i, r in enumerate(self.game_board):
            print(r)
            if i != 2:
                print("----+----+----")

    def print_moves(self):
        remaining = []
        for move in self.available_moves:
            if move != 0:
                remaining.append(str(move))
        print(f"Available Moves: {', '.join(remaining)}")
