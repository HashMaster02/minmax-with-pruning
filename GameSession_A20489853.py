from Game_A20489853 import Game
from AI_A20489853 import AI

"""
This class is a container for a single game session and keeps track of whether the sessions is currently
running, the winner (if there is one), the I/O logic and the MODE.
"""


class GameSession:

    def __init__(self, first_player):
        self.game = Game(first_player)
        self.in_session = True
        self.winner = None

    def human_vs_ai(self, ai_algorithm):

        bot = AI()

        # Using MinMax algorithm for AI
        if ai_algorithm == 1:
            while self.in_session:
                # Human's turn
                self.game.current_state()

                selection = int(input("Play: "))
                if selection == 0:
                    self.in_session = False
                    break

                valid = self.game.play_move(selection)
                if not valid:
                    continue

                self.winner = self.game.has_ended()
                if self.winner:
                    break

                self.game.next_player()
                self.game.board.print_board()
                print("___________________________________")

                # AI's turn
                (selection, value) = bot.min_max(self.game)
                self.game.play_move(selection)
                print(f"{self.game.current_player}'s selected move: {selection}. "
                      f"Number of search tree nodes generated: {bot.total_nodes}")
                bot.total_nodes = 0

                self.winner = self.game.has_ended()
                if self.winner:
                    break
                self.game.next_player()
                print("___________________________________")

        # Using MinMax with a-b Pruning algorithm for AI
        elif ai_algorithm == 2:
            while self.in_session:
                # Human's turn
                self.game.current_state()

                selection = int(input("Play: "))
                if selection == 0:
                    self.in_session = False
                    break

                valid = self.game.play_move(selection)
                if not valid:
                    continue

                self.winner = self.game.has_ended()
                if self.winner:
                    break

                self.game.next_player()
                self.game.board.print_board()
                print("___________________________________")

                # AI's turn
                (selection, value) = bot.alpha_beta_pruning(self.game, -10000, 10000)
                self.game.play_move(selection)
                print(f"{self.game.current_player}'s selected move: {selection}. "
                      f"Number of search tree nodes generated: {bot.total_nodes}")
                bot.total_nodes = 0

                self.winner = self.game.has_ended()
                if self.winner:
                    break
                self.game.next_player()
                print("___________________________________")

        return self.results()

    def ai_vs_ai(self, ai_algorithm):

        bot = AI()

        # Using MinMax algorithm for AI
        if ai_algorithm == 1:
            while self.in_session:

                (selection, value) = bot.min_max(self.game)
                self.game.play_move(selection)
                print(f"{self.game.current_player}'s selected move: {selection}. "
                      f"Number of search tree nodes generated: {bot.total_nodes}")
                bot.total_nodes = 0
                self.game.board.print_board()

                self.winner = self.game.has_ended()
                if self.winner is not None:
                    break
                self.game.next_player()
                print("___________________________________")

        # Using MinMax with a-b Pruning algorithm for AI
        elif ai_algorithm == 2:
            while self.in_session:

                (selection, value, _, _) = bot.alpha_beta_pruning(self.game,  -10000, 10000)
                self.game.play_move(selection)
                print(f"{self.game.current_player}'s selected move: {selection}. "
                      f"Number of search tree nodes generated: {bot.total_nodes}")
                bot.total_nodes = 0
                self.game.board.print_board()

                self.winner = self.game.has_ended()
                if self.winner is not None:
                    break
                self.game.next_player()
                print("___________________________________")

        return self.results()

    def results(self):
        if not self.in_session:
            return "You quit the game."

        else:
            if self.winner == "TIE":
                print("___________________________________")
                self.game.board.print_board()
                return "TIE"
            else:
                print("___________________________________")
                self.game.board.print_board()
                return f"{self.winner} WON!\n{"X's" if self.winner == "O" else "O"} LOST"
