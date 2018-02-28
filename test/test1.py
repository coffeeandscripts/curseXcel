#!/usr/env/bin python3

import curses

def main(stdscr):
    x = 0
    while (x != 'q'):
        stdscr.clear()
        stdscr.refresh()
        x = stdscr.getkey()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
