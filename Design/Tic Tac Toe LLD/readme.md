# 🟢 Tic-Tac-Toe Game

A simple console-based Tic-Tac-Toe game implemented in Python using object-oriented programming (OOP) concepts.

---

## 📂 **Project Req.**

---
The Tic-Tac-Toe game should be played on a 3x3 grid.

Two players take turns marking their symbols (X or O) on the grid.

The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.

If all the cells on the grid are filled and no player has won, the game ends in a draw.

The game should have a user interface to display the grid and allow players to make their moves.

The game should handle player turns and validate moves to ensure they are legal.

The game should detect and announce the winner or a draw at the end of the game.

## 🛠️ **Classes and Design**

### 1. 🟩 **Class: GameBoard**
Manages the game board and handles moves, win, and draw conditions.

| **Attribute/Method**     | **Description**                            |
|--------------------------|--------------------------------------------|
| `board`                  | 2D list representing the grid             |
| `moves`                  | Counter for the number of moves           |
| `__init__()`             | Initializes a 3x3 grid and resets moves   |
| `print_board()`          | Prints the current state of the board     |
| `make_move(row, col)`    | Places a marker if the cell is valid      |
| `check_for_draw()`       | Returns `True` if all cells are filled    |
| `check_for_win()`        | Checks for winning rows, cols, diagonals  |

### 2. 🟩 **Class: Player**
Represents a player with a name and marker (X or O).

| **Attribute/Method**     | **Description**                          |
|--------------------------|------------------------------------------|
| `name`                   | Player's name                           |
| `marker`                 | Player's symbol (X or O)                |
| `__init__(name, marker)` | Initializes a player                    |
| `get_name()`             | Returns the player’s name               |
| `get_marker()`           | Returns the player’s marker             |

### 3. 🟩 **Class: Game**
Controls the game flow and handles player turns, input, and result checking.

| **Attribute/Method**     | **Description**                          |
|--------------------------|------------------------------------------|
| `player1`, `player2`     | Player instances                        |
| `board`                  | GameBoard instance                      |
| `current_player`         | Tracks whose turn it is                 |
| `__init__(player1, player2)` | Initializes the game                  |
| `play()`                 | Starts the game loop                    |
| `switch_player()`        | Switches the turn between players       |
| `check_move(prompt)`     | Validates player input (0-2 for grid)   |

### 4. 🟩 **Class: TicTacToe**
The entry point to start the game.

| **Method**               | **Description**                          |
|--------------------------|------------------------------------------|
| `run()`                  | Creates players and starts the game     |

---

## 📊 **UML Diagram**

```
+-----------------+               +----------------+               +----------------+
|   GameBoard     |               |    Player      |               |     Game       |
+-----------------+               +----------------+               +----------------+
| - board         |               | - name         |               | - player1      |
| - moves         |               | - marker       |               | - player2      |
+-----------------+               +----------------+               | - board        |
| + print_board() |               | + get_name()   |               | - current_player|
| + make_move()   |               | + get_marker() |               +----------------+
| + check_for_win()|               +----------------+               | + play()       |
| + check_for_draw()|                                               | + switch_player|
+-----------------+                                               | + check_move()  |
                                                                  +----------------+
```


