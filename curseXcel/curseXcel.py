import ncurses

class ThrowError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr.value)

class Table():
    def __init__(self, win, cols, rows, width, height, col_names):
        self.win = win
        self.cols = cols
        self.rows = rows
        self.cell = (0, 0)
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

    def print_table(self):
        pass

    def set_column_header(self, value, col):
        if this.col_names == True:
            self.table[0][col] = value
        else:
            raise ThrowError("Set col_names boolean True")

    def shift_columns_right(self):
        if self.shown_column < self.cols:
            self.shown_column += 1

    def shift_columns_left(self):
        if self.shown_column > 0:
            self.shown_column -= 1

    def shift_rows_up(self):
        if self.shown_row > 0:
            self.shown_row -= 1

    def shift_rows_down(self):
        if self.shown_row < self.rows:
            self.shown_row += 1

    def cell_left(self):
        pass

    def cell_right(self):
        pass

    def cell_up(self):
        pass

    def cell_down(self):
        pass

    def delete_column(self):
        pass

    def delete_row(self):
        pass

    def clear_cell(self):
        pass

    def clear_row(self):
        pass

    def clear_column(self):
        pass
