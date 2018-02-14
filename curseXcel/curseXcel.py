import ncurses

class Table():
    def __init__(self, win, cols, rows, cell):
        self.win = win
        self.cols = cols
        self.rows = rows
        self.cell = cell
        self.generate_table()

    def generate_table(self):
        self.table = [None] * rows
        for x in self.table:
            x = [None] * cols
