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
            return True
        return False

    def undo_move(self, position: int):
        self.board.undo_move(position)
        self.next_player()

    def next_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def has_ended(self):
        return self.board.check_win_conditions()

    def current_state(self):
        print(f"{self.current_player}'s move. What is your move (possible moves at the moment are: "
              f"{self.board.available_moves} | enter 0 to exit the game)?")
        self.board.print_board()
