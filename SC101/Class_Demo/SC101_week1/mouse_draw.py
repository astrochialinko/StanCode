"""
File: mouse_draw.py
Name: Chia-Lin Ko
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged

# This constant controls the size of the pen stroke
SIZE = 15
COLOR = 'dodgerblue'
COLOR2 = 'deeppink'

# Global variable
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

def main():
	onmousedragged(draw)


def draw(mouse):
	stroke = GRect(SIZE, SIZE, x = mouse.x-SIZE/2, y = mouse.y-SIZE/2)
	if (mouse.x -SIZE/2) < (WINDOW_WIDTH/2):
		stroke.filled = True
		stroke.color = COLOR
		stroke.fill_color = COLOR
	else:
		stroke.filled = True
		stroke.color = COLOR2
		stroke.fill_color = COLOR2
	window.add(stroke)



if __name__ == '__main__':
	main()
