import sys
from GameSession_A20489853 import GameSession as Session

if __name__ == "__main__":

    # TODO: Verify CLI inputs

    ALGO, FIRST, MODE = sys.argv[1], sys.argv[2], sys.argv[3]

    # Print assignment information
    print(f"last_name, first_name, AXXXXXXX solution: \n"
          f"Algorithm: {ALGO} \n"
          f"First: {FIRST} \n"
          f"Mode: {MODE} \n")

    # Start Human vs. AI session
    if int(MODE) == 1:
        game = Session(FIRST)
        results = game.human_vs_ai(int(ALGO))
        print(results)

    # Start AI vs. AI session
    elif int(MODE) == 2:
        game = Session(FIRST)
        results = game.ai_vs_ai(int(ALGO))
        print(results)