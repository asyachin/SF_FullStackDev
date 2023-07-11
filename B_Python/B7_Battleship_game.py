from random import randint

class BoardOutException(Exception):
    def __str__(self):
        return "You are out of the board"

class BoardUsedException(Exception):
    def __str__(self):
        return "You have already shot here"

class BoardWrongShipException(Exception):
    pass

class BoardException(Exception):
    pass

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        around = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for d in ship.dots:
            for dx, dy in around:
                cur = Dot(d.x + dx, d.y + dy)
                if not self.out(cur) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()
        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Ship is destroyed!")
                    return False
                else:
                    print("Ship is damaged!")
                    return True

        self.field[d.x][d.y] = "."
        print("You missed!")
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                shot = self.enemy.shot(target)
                return shot
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"AI is shooting at {d.x + 1} {d.y + 1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Your turn: ").split()

            if len(cords) != 2:
                print("Enter 2 coordinates!")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Enter numbers!")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

class Game:
    def __init__(self, size=6):
        self.lens = [3, 2, 2, 1, 1, 1, 1]
        self.size = size
        player = self.random_board()
        comp = self.random_board()
        comp.hid = True

        self.ai = AI(comp, player)
        self.us = User(player, comp)

    def try_board(self):
        board = Board(size=self.size)
        for l in self.lens:
            while True:
                try:
                    board.add_ship(Ship(Dot(randint(0, 5), randint(0, 5)), l, randint(0, 1)))
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("-------------------")
        print("  Welcome to Sea Battle!")
        print("-------------------")
        print("  Try to beat the AI!")
        print("-------------------")
        print("  Format: x y")
        print("  x - row, y - column")
        print("-------------------")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Player's board:")
            print(self.us.board)
            print("-" * 20)
            print("AI's board:")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print("Player's turn!")
                shot = self.us.move()
            else:
                print("AI's turn!")
                shot = self.ai.move()
            if shot:
                num -= 1

            if self.ai.board.defeat():
                print("-" * 20)
                print("Player won!")
                break

            if self.us.board.defeat():
                print("-" * 20)
                print("AI won!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()
