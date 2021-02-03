"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect, GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmouseclicked, onmousedragged

# This constant controls the size of the GRect
SIZE = 20
COLOR = 'dodgerblue'

# Global variable
window = GWindow()
rect = GRect(SIZE, SIZE)


def main():
	window.add(rect)
	rect.filled = True
	rect.color = COLOR
	rect.fill_color = COLOR
	onmousemoved(reset_position)
	onmouseclicked(my_punch)
	onmousedragged(draw)


def draw(mouse):
	stroke = GRect(SIZE, SIZE, x = mouse.x-SIZE/2, y = mouse.y-SIZE/2)
	stroke.filled = True
	stroke.color = COLOR
	stroke.fill_color = COLOR
	window.add(stroke)


def my_punch(m):
	hole = GRect(SIZE, SIZE, x = m.x-SIZE/2, y = m.y-SIZE/2)
	hole.filled = True
	hole.color = COLOR
	hole.fill_color = COLOR
	window.add(hole)


def reset_position(event):
	rect.x = event.x - rect.width/2
	rect.y = event.y - rect.height/2






if __name__ == '__main__':
	main()
