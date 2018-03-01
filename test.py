#!/usr/env/bin python3

import curses
from curseXcel.curseXcel import Table

def main(stdscr):
    x = 0
    table = Table(stdscr, 4, 6, 5, 22, 3, 0)
    table.set_cell(1, 0, "test")
    m = 0
    while m < 4:
        n = 0
        while n < 6:
            table.set_cell(m, n, n+m)
            n += 1
        m += 1
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
