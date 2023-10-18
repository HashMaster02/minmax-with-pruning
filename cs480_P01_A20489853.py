import sys
from Game_A20489853 import Game

if __name__ == "__main__":

    playing = True
    game = Game("X")
    winner = ''

    while playing:
        game.current_state()
        selection = int(input("Play: "))
        if selection == 0:
            playing = False
            break
        game.play_move(selection)
        winner = game.has_ended()
        if winner != '':
            break
        print("___________________________________")

    if not playing:
        print("You quit the game.")

    else:
        if winner == 'Draw':
            print("The game was a draw.")
        else:
            print(f"{winner} wins!")

# TODO: Make a function that chooses a random position to act as the placeholder for the AI
