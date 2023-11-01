"""
This class models the board for any tic tac toe game. It maintains the state of the board, the currently
available moves, and functions to make and undo moves, check whether the game has ended (win or tie), and
print the current board state.
"""


class Board:

    def __init__(self):
        self.game_board = [[' ', ' ', ' '],
                           [' ', ' ', ' '],
                           [' ', ' ', ' ']]
        self.available_moves = [1, 2, 3, 4, 5, 6, 7, 9, 8]
        self.winning_cells = [(1,2,3), (4,5,6), (7,8,9),
                              (1,4,7), (2,5,8), (3,6,9),
                              (1,5,9), (3,5,7)]

    def make_move(self, position: int, player: str):

        try:
            self.available_moves.index(position) # check if move is available
            self.game_board[(position - 1) // 3][(position % 3) - 1] = player
            self.available_moves.remove(position)
            return True
        except ValueError:
            print("Illegal move. Try again.")
            return False

    def undo_move(self, position: int):
        self.game_board[(position - 1) // 3][(position % 3) - 1] = ' '
        self.available_moves.append(position)
        self.available_moves.sort()

    def check_win_conditions(self):
        for (x, y, z) in self.winning_cells:
            if (
                self.get_position(x) == self.get_position(y) == self.get_position(z) == "X"
                or self.get_position(x) == self.get_position(y) == self.get_position(z) == "O"
                ):
                return self.get_position(x)

        if len(self.available_moves) == 0:
            return 'TIE'

        return None

    def get_position(self, position):
        return self.game_board[(position - 1) // 3][(position % 3) - 1]

    def print_board(self):
        for i, r in enumerate(self.game_board):
            print(
                f"  {r[0]}  |  {r[1]}  |  {r[2]}  "
            )
            if i != 2:
                print("-----+-----+-----")
