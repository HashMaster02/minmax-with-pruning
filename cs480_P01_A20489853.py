import sys
from GameSession_A20489853 import GameSession as Session

if __name__ == "__main__":

    # ALGO, FIRST, MODE = sys.argv[1], sys.argv[2], sys.argv[3]
    ALGO = 1
    FIRST = "X"
    MODE = 2
    print(f"last_name, first_name, AXXXXXXX solution: \n"
          f"Algorithm: {ALGO} \n"
          f"First: {FIRST} \n"
          f"Mode: {MODE} \n")

    if int(MODE) == 1:
        game = Session(FIRST)
        results = game.human_vs_ai(int(ALGO))
        print(results)

    elif int(MODE) == 2:
        game = Session(FIRST)
        results = game.ai_vs_ai(int(ALGO))
        print(results)
