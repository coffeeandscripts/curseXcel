#!/usr/env/bin python3

import curses
from curseXcel.curseXcel import Table

def main(stdscr):
    x = 0
    table = Table(stdscr, 4, 6, 5, 20, 30, spacing=1, col_names=True)
    m = 0
    while m < 6:
        table.set_column_header("Col " + str(m+1), m)
        m += 1
    m = 0
    while m < 4:
        n = 0
        while n < 6:
            table.set_cell(m, n, n+m)
            n += 1
        m += 1
    table.delete_row(2)
    while (x != 'q'):
        table.refresh()
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
