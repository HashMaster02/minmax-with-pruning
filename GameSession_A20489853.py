from Game_A20489853 import Game
from AI_A20489853 import AI


class GameSession:

    def __init__(self, first_player):
        self.game = Game(first_player)
        self.in_session = True
        self.winner = ''

    def human_vs_ai(self, ai_algorithm):

        bot = AI()
        if ai_algorithm == 0:
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
                self.game.next_player()

                self.winner = self.game.has_ended()
                if self.winner != '':
                    break

                self.game.board.print_board()
                print("___________________________________")

                # AI's turn
                selection = bot.random_spot(self.game.board.available_moves)
                self.game.play_move(selection)
                print(f"{self.game.current_player}'s selected move: {selection}.")
                self.game.next_player()

                self.winner = self.game.has_ended()
                if self.winner != '':
                    break
                print("___________________________________")

            return self.results()

    def ai_vs_ai(self, ai_algorithm):
        bot = AI()
        if ai_algorithm == 0:
            while self.in_session:

                selection = bot.random_spot(self.game.board.available_moves)
                print(f"{self.game.current_player}'s selected move: {selection}.")
                self.game.play_move(selection)
                self.game.board.print_board()
                self.game.next_player()

                self.winner = self.game.has_ended()
                if self.winner != '':
                    break
                print("___________________________________")
            return self.results()

    def results(self):
        if not self.in_session:
            return "You quit the game."

        else:
            if self.winner == 'TIE':
                return "TIE"
            else:
                return f"{self.winner} WON!"
