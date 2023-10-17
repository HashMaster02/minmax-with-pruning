from Board_A20489853 import Board


class Game:

    def __init__(self, first_turn: str):
        self.board = Board()
        self.player_1 = first_turn
        self.player_2 = 'O' if first_turn == 'X' else 'X'
        self.current_player = first_turn

    def play_move(self, position: int):
        valid = self.board.make_move(position, self.current_player)
        if valid:
            self.next_player()

    def next_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def current_state(self):
        print(f"It is {self.current_player}'s turn. Select a move or type '0' to quit.")
        self.board.print_moves()
        self.board.print_board()
