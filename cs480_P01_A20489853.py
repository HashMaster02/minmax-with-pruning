import sys
from GameSession_A20489853 import GameSession as Session

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("LENGTH ERROR")
        print("ERROR: Not enough/too many/illegal input arguments.")
        sys.exit()

    ALGO, FIRST, MODE = sys.argv[1], sys.argv[2], sys.argv[3]

    if not (ALGO == "1" or ALGO == "2") or not (FIRST == "O" or FIRST == "X") or not (MODE == "1" or MODE == "2"):
        print("ERROR: Not enough/too many/illegal input arguments.")
        sys.exit()

    # Print assignment information
    print(f"last_name, first_name, AXXXXXXX solution: \n"
          f"Algorithm: {"MiniMax" if ALGO == "1" else "MiniMax with alpha-beta pruning"} \n"
          f"First: {FIRST} \n"
          f"Mode: {"human vs. computer" if MODE == '1' else "computer vs. computer"} \n")

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
