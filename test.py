#!/usr/env/bin python3

import curses
from curseXcel.curseXcel import Table

def main(stdscr):
    x = 0
    table = Table(stdscr, 4, 6, 3, 20, 30, spacing=1, col_names=True)
    table.set_cell(1, 0, "test")
    table.set_column_header(str(6), 5)
    m = 0
    while m < 4:
        n = 0
        while n < 6:
            table.set_cell(m, n, n+m)
            n += 1
        m += 1
    table.delete_row(2)
    while (x != 'q'):
        stdscr.clear()
        table.print_table()
        stdscr.refresh()
        x = stdscr.getkey()
        if (x == 'j'):
            table.cursor_left()
        elif (x == 'l'):
            table.cursor_right()
        elif (x == 'k'):
            table.cursor_down()
        elif (x == 'i'):
            table.cursor_up()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
