#!/usr/env/bin python3

import curses
from curseXcel.curseXcel import Table

def main(stdscr):
    x = 0
    table = Table(stdscr, 4, 6, 5, 50, 20, 0)
    table.set_cell(1, 0, "test")
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
