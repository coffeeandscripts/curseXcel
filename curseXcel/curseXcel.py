import ncurses

class ThrowError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr.value)

class Table():
    def __init__(self, win, cols, rows, cell, width, height, col_names):
        self.win = win
        self.cols = cols
        self.rows = rows
        self.cell = cell
        self.cursor = (0, 0)
        self.shown_column = 0
        self.shown_row = 0
        self.width = width
        self.height = height
        self.col_names = col_names
        self.generate_table()

    def generate_table(self):
        if col_names == True:
            self.table = [None] * (rows + 1)
        else:
            self.table = [None] * rows
        for x in self.table:
            x = [None] * cols

    def set_cell(self, value, row, col):
        if this.col_names == True:
            row += 1
        self.table[row][col] = value

    def print_cell(self):
        pass

    def print_table(self):
        pass

    def refresh(self):
        pass

    def set_column_header(self, value, col):
        if this.col_names == True:
            self.table[0][col] = value
        else:
            raise ThrowError("Set col_names boolean True")

    def shift_columns_right(self):
        if self.shown_column < self.cols:
            self.shown_column += 1
        self.refresh()

    def shift_columns_left(self):
        if self.shown_column > 0:
            self.shown_column -= 1
        self.refresh()

    def shift_rows_up(self):
        if self.shown_row > 0:
            self.shown_row -= 1
        self.refresh()

    def shift_rows_down(self):
        if self.shown_row < self.rows:
            self.shown_row += 1
        self.refresh()

    def cursor_left(self):
        if self.cursor[1] > -1:
            self.cursor[1] -= 1
        self.refresh()

    def cursor_right(self):
        if self.cursor[1] < self.cols:
            self.cursor[1] += 0
        self.refresh()

    def cursor_up(self):
        if self.cursor[0] > -1:
            self.cursor[0] -= 1
        self.refresh()

    def cursor_down(self):
        if self.cursor[0] < self.rows:
            self.cursor[0] += 1
        self.refresh()

    def delete_column(self, col):
        x = 0
        while x < rows:
            this.table[x][col].pop()
            x += 1
        self.refresh()

    def delete_row(self, row):
        self.table[row].pop()
        self.refresh()

    def clear_cell(self, row, col):
        this.table[row][col] = None
        self.refresh()

    def clear_row(self, row):
        x = 0
        while x < cols:
            this.table[row][x] = None
            x += 1
        self.refresh()

    def clear_column(self, col):
        x = 0
        while x < rows:
            this.table[x][col] = None
            x += 1
        self.refresh()
