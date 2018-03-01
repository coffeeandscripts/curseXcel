import curses

class ThrowError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr.value)

class Table():
    def __init__(self, win, rows, cols, cell, width, height, col_names):
        self.win = win
        self.cols = cols
        self.rows = rows
        self.cell = cell
        self.cursor = [-1, -1]
        self.shown_column = 0
        self.shown_row = 0
        self.width = width
        self.height = height
        self.col_names = col_names
        self.generate_table()

    def generate_table(self):
        rows = self.rows
        if self.col_names == True:
            row += 1
        self.table = []
        x = 0
        while x < rows:
            self.table.append([""] * self.cols)
            x += 1

    def set_cell(self, row, col, value):
        if self.col_names == True:
            row += 1
        self.table[row][col] = str(value)

    def set_word(self, val):
        if len(val) > self.cell:
            val = val[:self.cell-2]
            val = val + '..'
        elif len(val) < self.cell:
            x = len(val)
            while x < self.cell:
                val = ' ' + val
                x += 1
        return val

    def print_cell(self, y, x, val, hl, length):
        if hl == True:
            self.win.addstr(y, x, (self.set_word(val))[:length], curses.A_REVERSE)
        else:
            self.win.addstr(y, x, (self.set_word(val))[:length])

    def calc_max_shown(self, length, chars):
            return(round(length/chars), length%chars)

    def set_highlight(self, y, x):
        boolRet = False
        if (self.cursor[0] == y or self.cursor[0] == -1) and (self.cursor[1] == x or self.cursor[1] == -1):
            boolRet = True
        return boolRet

    def print_table(self):
        max_cols = self.calc_max_shown(self.width, self.cell)
        max_rows = self.calc_max_shown(self.height, 1)
        y = 0
        while y < max_rows[0] and y < self.rows:
            x = 0
            while x < max_cols[0] and x < self.cols:
                self.print_cell(y, x*self.cell, self.set_word(self.table[y+self.shown_row][x+self.shown_column]), self.set_highlight(y+self.shown_row, x+self.shown_column), self.cell)
                x += 1
            y += 1

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
            if self.cursor[1] == self.shown_column - 1 and self.shown_column > 0:
                self.shown_column -= 1
        self.refresh()

    def cursor_right(self):
        max_cols = self.calc_max_shown(self.width, self.cell)
        if self.cursor[1] < self.cols - 1:
            self.cursor[1] += 1
            if self.cursor[1] - self.shown_column >= max_cols[0]:
                self.shown_column += 1
        self.refresh()

    def cursor_up(self):
        if self.cursor[0] > -1:
            self.cursor[0] -= 1
            if self.cursor[0] == self.shown_row -1 and self.shown_row > 0:
                self.shown_row -= 1
        self.refresh()

    def cursor_down(self):
        max_rows = self.calc_max_shown(self.height, 1)
        if self.cursor[0] < self.rows - 1:
            self.cursor[0] += 1
            if self.cursor[0] - self.shown_row >= max_rows[0]:
                self.shown_row += 1
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
