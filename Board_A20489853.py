
class Board:

    def __init__(self):
        self.game_board = [[' ', ' ', ' '],
                           [' ', ' ', ' '],
                           [' ', ' ', ' ']]
        self.available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def make_move(self, position: int, player: str):
        if self.available_moves[position - 1] == 0:
            print("___________________________________")
            print("Illegal move. Try again.")
            return False
        self.game_board[(position - 1) // 3][(position % 3) - 1] = player
        self.available_moves[position - 1] = 0
        return True

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
