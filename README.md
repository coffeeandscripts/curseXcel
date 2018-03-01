# curseXcel
python ncurses library to generate, print and manipulate tables

## Features
A simple solution to tabulating information and data direct within the terminal. Using the famous ncurses module for python, curseXcel lets you customise and fill your table with ease, and then quickly present it anywhere on the terminal window.

If the table extends beyond the limits of the screen that you have set, curseXcel allows you to scroll across the x and y planes to find you information.

As always, a picture says a thousand words:
![Screenshot](https://raw.githubusercontent.com/coffeeandscripts/curseXcel/master/example.png "curseXcel example")

## Usage
First you need to follow standard ncurses procedure to create your screen and/or window.
~~~
import curses

def main(stdscr):
	x = 0
	while ( != 'q'):
		stdscr.refresh()
		x = stdscr.getkey()

stdscr = curses.initscr
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
~~~

Then you are free to create your table. Some variables are essential, while others a customisable:
~~~
from curseXcel import Table
table = Table(win, rows, cols, cell, width, height, col_names=None, spacing=None)   # the last two are optional
~~~
Here is an example put together:
~~~
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
table.refresh()
~~~

An extended test file is included.

Below are each of the functions that can be used and their usage:
~~~
Table.cursor() 				# returns the cursor position as a tuple
Table.set_cell(row, col, value) 	# places a string into a cell
Table.print_table() 			# prints the table to the screen
Table.refresh() 			# clears the screen, prints table then refreshes screen
Table.cell() 				# returns the contents of a cell as a string
Table.set_column_header(value, col) 	# places a string into the column header if set
Table.cursor_left() 			# moves cursor left
Table.cursor_right() 			# moves cursor right
Table.cursor_up() 			# moves cursor up
Table.cursor_down() 			# moves cursor down
Table.delete_column(col) 		# deletes the column from the table
Table.delete_row(row) 			# deletes the row from the table
Table.clear_cell(row, col) 		# removes the contents of a cell
Table.clear_row(row) 			# removes all the contents of a row
Table.clear_column(col) 		# removes all the contents of a column
~~~
## Quickstart guide

### Dependencies

- curses (should be installed in standard library)

There are multiple installation methods:

**Make sure you are running python3**

### PyPI

~~~~
> sudo pip install curseXcel			# may have to run pip3
~~~~

### Manual

- download file to a location of choice

~~~~
> cd 'path'
> sudo python3 setup.py install		# can use just python if error
~~~~

### Uninstall

~~~
> sudo pip uninstall curseXcel
~~~

## Licence
curseXcel - create tables with ncurses

Copyright (c) 2017 coffeeandscripts

coffeeandscripts.github.io

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
