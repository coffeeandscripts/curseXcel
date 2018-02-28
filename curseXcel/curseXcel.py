import ncurses

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

    def set_cell(self):
        pass

    def print_table(self):
        pass

    def set_column_header(self):
        pass

    def shift_columns(self):
        pass

    def shift_rows(self):
        pass

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
