# Tic Tac Toe AI

This is a fully playable tic tac toe game with an AI implementation using the Minimax
and Minimax with alpha-beta pruning algorithms. It is a CLI application and is built
using Python3.

This was a project for a college class titled *Introduction to Artificial Intelligence*.

## Game Setup
The game can be played using 2 different algorithms for the AI (minimax, minimax
with alpha-beta pruning), 2 different modes (human vs. AI, AI vs. AI), and you can 
specify who goes first (X's or O's). 

The command line arguments are passed-in as follows:
```commandline
python cs480_P01_A20489853.py ALGO FIRST MODE
```

* **ALGO**
  * 1: MiniMax
  * 2: Minimax with alpha-beta pruning
* **FIRST**
  * X: X goes first
  * O: O goes first
* **MODE**
  * 1: Human vs. AI
  * 2: AI vs. AI

For example, the following command will start a human vs. AI game where X goes first and
the AI uses the Minimax algorithm to choose its move:
```commandline
python cs480_P01_A20489853.py 1 X 1
```

## How to Play
1. Clone the repository using the following command
```commandline
git clone https://github.com/HashMaster02/minmax-with-pruning
```

2. Open a command line and run the command mentioned in **Game Setup**. Ensure you pass-in
legal arguments
3. Follow the instructions on-screen
