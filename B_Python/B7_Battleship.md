
The essence of the written application is the game "Battleship."
The application interface should be a console window with two 6x6 fields.
The player plays against the computer. The computer makes random moves but does not shoot at cells it has already targeted.
To represent a ship, describe a Ship class with a constructor that takes a set of points (coordinates) on the game board.
Describe the Board class. The board should accept a set of ships in its constructor.
Ships should be at least one cell away from each other.
Each board (for the AI and the player) should have the following number of ships: 1 ship with 3 cells, 2 ships with 2 cells, and 4 ships with 1 cell.
Prohibit the player from shooting at the same cell multiple times. If the player makes a move error, an exception should be raised.
Handle unexpected situations by throwing and handling exceptions.
The winner is determined by whoever destroys the opponent's ships faster.
