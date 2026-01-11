# 🎮 Tic-Tac-Toe (Python, OOP)

Play with the game on Replit here: https://replit.com/@mailprithvi/TicTacToe

This is a **console-based Tic-Tac-Toe game** implemented in **Python** using **Object-Oriented Programming (OOP)** principles.

The goal of this project is to practice designing clean classes, working with objects, and building game logic by letting objects interact with each other.

A human player plays against a computer player that selects random moves.

---

## 📌 Game Rules

- The game is played on a **3×3 board**
- Board positions are numbered from **1 to 9**
```text
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
```

- Human player uses marker **X**
- Computer player uses marker **O**
- Players take turns placing their marker on the board
- If a player selects a position that is already taken, the player **loses the turn**
- A player wins by filling:
  - Any row
  - Any column
  - The diagonal
  - The anti-diagonal
- If the board is full and no player has won, the game ends in a **tie**
- After the game ends, the user can choose to start a new round

---

## 🧱 Project Structure

The project is built using the following classes:

### Move
- Represents a single move in the game
- Stores the board position (1–9)
- Stores the player's marker (`X` or `O`)

### Player
- Represents a player (human or computer)
- Stores the player name and marker
- Generates the next move
- The computer player selects a random available position

### Board
- Represents the game board
- Stores the board state
- Displays the board
- Validates moves
- Checks for winning conditions
- Detects a full board (tie)

---

## 🧪 Example Output
```
**************************
  Welcome to Tic-Tac-Toe  
**************************

Please enter your move (1-9): 4
Computer move (1-9): 8
Awesome. You won the game! 🎉

```
---

## 📦 Requirements

Python 3.8 or higher

No external Python libraries are required

The project uses only the Python standard library

---

## ▶️ How to Run the Game

1. Make sure Python is installed:
```bash
python --version
```

2. Run the game
```bash
python main.py
```

---



