from Game_A20489853 import Game
from AI_A20489853 import random_spot


class GameSession:

    def __init__(self, first_player):
        self.game = Game(first_player)
        self.in_session = True
        self.winner = ''

    def human_vs_human(self):
        while self.in_session:
            self.game.current_state()
            selection = int(input("Play: "))

            if selection == 0:
                self.in_session = False
                break

            self.game.play_move(selection)

            self.winner = self.game.has_ended()
            if self.winner != '':
                break
            print("___________________________________")

        return self.results()

    def human_vs_ai(self, ai_algorithm):

        if ai_algorithm == 0:
            while self.in_session:

                # Human's turn
                self.game.current_state()
                selection = int(input("Play: "))
                if selection == 0:
                    self.in_session = False
                    break
                self.game.play_move(selection)
                self.winner = self.game.has_ended()
                if self.winner != '':
                    break
                print("___________________________________")

                # AI's turn
                self.game.current_state()
                selection = random_spot(self.game.board.available_moves)
                self.game.play_move(selection)
                self.winner = self.game.has_ended()
                if self.winner != '':
                    break
                print("___________________________________")

            return self.results()

    def ai_vs_ai(self, ai_algorithm):

        if ai_algorithm == 0:
            while self.in_session:
                self.game.current_state()
                selection = random_spot(self.game.board.available_moves)
                self.game.play_move(selection)
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

