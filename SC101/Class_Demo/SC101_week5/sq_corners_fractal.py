"""
File: sq_corners_fractal.py
Name: Chia-Lin Ko
-----------------------------------
This program draws a fractal with GRect on GWindow.
Students will find it useful to understand the order
of each recursive calls.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GRect
from campy.gui.events.timer import pause

# Constants
SIZE = 300      # It controls the width and height of the GRect on canvas
LEVEL = 3       # It controls the recursive depth of fractal

# This is the canvas for GRect
window = GWindow(width=1000, height=700)


def main():
	center_x = window.width/2
	center_y = window.height/2
	draw_rect(LEVEL, SIZE, center_x, center_y)


def draw_rect(level, width, center_x, center_y):
	if level == 0:
		pass
	else:
		rect = GRect(width, width, x=center_x-width/2, y=center_y-width/2)
		rect.filled = True
		# rect.color = 'snow'
		rect.fill_color = 'snow'

		# Upper left
		draw_rect(level-1, width/2, center_x-width/2, center_y-width/2)
		# Lower right
		draw_rect(level - 1, width / 2, center_x + width / 2, center_y + width / 2)

		window.add(rect)

		# Upper right
		draw_rect(level - 1, width / 2, center_x + width / 2, center_y - width / 2)
		# Lower left
		draw_rect(level - 1, width / 2, center_x - width / 2, center_y + width / 2)





if __name__ == '__main__':
	main()
