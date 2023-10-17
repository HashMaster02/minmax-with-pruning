import sys
from Game_A20489853 import Game

if __name__ == "__main__":

    playing = True
    game = Game("X")

    while playing:
        game.current_state()
        selection = int(input("Play: "))
        if selection == 0:
            break
        game.play_move(selection)
        print("___________________________________")

    print("___________________________________")
    print("You quit the game.")

# TODO: Check if we arrived at a terminal state using DFS
