import curses

class Table():
    def __init__(self, win, rows, cols, cell, width, height, col_names=None, spacing=None):
        self.win = win
        self.cols = cols
        self.rows = rows
        self.cell = cell
        self.cursor = [-1, -1]
        self.shown_column = 0
        self.shown_row = 0
        self.width = width
        self.height = height
        if spacing == None:
            self.spacing = 0
        else:
            self.spacing = spacing
        if col_names == None:
            self.col_names = False
        else:
            self.col_names = col_names
            self.rows += 1
        if self.win.getmaxyx()[0] < self.height:
            raise Exception("table y printing outside of range")
        if self.win.getmaxyx()[1] < self.width:
            raise Exception("table x printing outside of range")
        self.generate_table()

    def generate_table(self):
        rows = self.rows
        self.table = []
        x = 0
        while x < rows:
            self.table.append([""] * self.cols)
            x += 1

    def cursor(self):
        return (self.cursor[0], self.cursor[1])

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
        max_cols = self.calc_max_shown(self.width, self.cell+self.spacing)
        max_rows = self.calc_max_shown(self.height, 1)
        y = 0
        while y < max_rows[0] and y < self.rows:
            x = 0
            while x < max_cols[0] and x < self.cols:
                if self.col_names == True and y == 0:
                    self.print_cell(y, x*self.cell+x*self.spacing, self.set_word(self.table[0][x+self.shown_column]), self.set_highlight(y+self.shown_row, x+self.shown_column), self.cell)
                else:
                    self.print_cell(y, x*self.cell+x*self.spacing, self.set_word(self.table[y+self.shown_row][x+self.shown_column]), self.set_highlight(y+self.shown_row, x+self.shown_column), self.cell)
                x += 1
            y += 1

    def cell(self):
        return self.table[cursor[0]][cursor[1]]

    def refresh(self):
        self.win.clear()
        self.print_table()
        self.win.refresh()

    def set_column_header(self, value, col):
        if self.col_names == True:
            self.table[0][col] = str(value)
        else:
            raise Exception("Set col_names boolean True")

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
        max_cols = self.calc_max_shown(self.width, self.cell+self.spacing)
        if self.cursor[1] < self.cols - 1:
            self.cursor[1] += 1
            if self.cursor[1] - self.shown_column >= max_cols[0]:
                self.shown_column += 1
        self.refresh()

    def cursor_up(self):
        if self.cursor[0] > -1:
            self.cursor[0] -= 1
            if self.col_names == False and self.cursor[0] == self.shown_row - 1 and self.shown_row > 0:
                self.shown_row -= 1
            if self.col_names == True and self.cursor[0] == self.shown_row and self.shown_row > 0:
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
        while x < self.rows:
            del self.table[x][col]
            x += 1
        self.cols -= 1
        self.refresh()

    def delete_row(self, row):
        if self.col_names == True:
            row += 1
        del self.table[row]
        self.rows -= 1
        self.refresh()

    def clear_cell(self, row, col):
        if self.col_names == True:
            row += 1
        self.table[row][col] = " "
        self.refresh()

    def clear_row(self, row):
        x = 0
        if self.col_names == True:
            row += 1
        while x < self.cols:
            self.table[row][x] = " "
            x += 1
        self.refresh()

    def clear_column(self, col):
        x = 0
        while x < self.rows:
            self.table[x][col] = " "
            x += 1
        self.refresh()
