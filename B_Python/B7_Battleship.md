
1. The essence of the written application is the game "Battleship."
2. The application interface should be a console window with two 6x6 fields.
3. The player plays against the computer. The computer makes random moves but does not shoot at cells it has already targeted.
4. To represent a ship, describe a Ship class with a constructor that takes a set of points (coordinates) on the game board.
5. Describe the Board class. The board should accept a set of ships in its constructor.
6. Ships should be at least one cell away from each other.
7. Each board (for the AI and the player) should have the following number of ships: 1 ship with 3 cells, 2 ships with 2 cells, and 4 ships with 1 cell.
8. Prohibit the player from shooting at the same cell multiple times. If the player makes a move error, an exception should be raised.
9. Handle unexpected situations by throwing and handling exceptions.
10. The winner is determined by whoever destroys the opponent's ships faster.
