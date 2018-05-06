import random

class Game:
    EMPTY_CELL = 0   
    NUBERS = [2, 4]

    def __init__(self, size):
        self.width = size
        self.score = 0
        self.field = [[self.EMPTY_CELL for col in range(size)] for row in range(size)]

        self.add_number(2, self.NUBERS[:1])

    def add_number(self, count, list_value):
        i = 0 

        while i < count:
            row = random.randint(0, self.width - 1)
            col = random.randint(0, self.width - 1)

            if self.field[row][col] == self.EMPTY_CELL:
                self.field[row][col] = random.choice(list_value)
                i += 1

    def move_left(self):
        cell = self._get_cell

        for row in range(self.width):
            for col in range(self.width - 1):
                for pos in range(self.width - 1 - col):
                    if cell(row, pos) == self.EMPTY_CELL and cell(row, pos + 1) != self.EMPTY_CELL:
                        self.field[row][pos], self.field[row][pos + 1] = self.field[row][pos + 1], self.field[row][pos] 
 
    def move_right(self):
        cell = self._get_cell
      
        for row in range(self.width):            
            for col in range(self.width - 1):
                for pos in range(self.width - 1, col, -1):
                    if cell(row, pos) == self.EMPTY_CELL and cell(row, pos - 1) != self.EMPTY_CELL:
                        self.field[row][pos], self.field[row][pos - 1] = self.field[row][pos - 1], self.field[row][pos] 

    def move_up(self):
        cell = self._get_cell

        for col in range(self.width):
            for row in range(self.width - 1):
                for pos in range(self.width - 1 - row):
                    if cell(pos, col) == self.EMPTY_CELL and cell(pos + 1, col) != self.EMPTY_CELL:
                        self.field[pos][col], self.field[pos + 1][col] = self.field[pos + 1][col], self.field[pos][col] 
 
    def move_down(self):
        cell = self._get_cell

        for col in range(self.width):
            for row in range(self.width - 1):
                for pos in range(self.width - 1, row, -1):
                    if cell(pos, col) == self.EMPTY_CELL and cell(pos - 1, col) != self.EMPTY_CELL:
                        self.field[pos][col], self.field[pos - 1][col] = self.field[pos - 1][col], self.field[pos][col] 
 
    def has_moves(self):
        for row in self.field:
            if self.EMPTY_CELL in row:
                return True
        return False 
 
    def get_score(self):
        return self.score
 
    def get_field(self):
        return self.field

    def _get_cell(self, row, col):
        return self.field[row][col]

 
 
def main():
    game = Game(4)
 
    while True:
        field = game.get_field()
        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))
 
        print("\033[H\033[J", end="")
        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(cell).rjust(cell_width)
                for cell in row
            )
            for row in field
        ))
 
        if not game.has_moves():
            print("No available moves left, game over.")
            break
 
        print("L, R, U, D - move")
        print("Q - exit")
 
        try:
            c = input("> ")
        except (EOFError, KeyboardInterrupt):
            break
 
        if c in ('l', 'L'):
            game.move_left()
            # game.add_number(2, game.NUBERS)
        elif c in ('r', 'R'):
            game.move_right()
            # game.add_number(2, game.NUBERS)
        elif c in ('u', 'U'):
            game.move_up()
            # game.add_number(2, game.NUBERS)
        elif c in ('d', 'D'):
            game.move_down()
            # game.add_number(2, game.NUBERS)
        elif c in ('q', 'Q'):
            break
 
    print("Bye!")
 
 
if __name__ ==  '__main__':
    main()