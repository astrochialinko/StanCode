"""
File: bouncing_rect.py
Name: Chia-Lin Ko
------------------------
This file shows how to make a simple 
animation by campy library
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause




# This controls the width and height of the rect
SIZE = 30
WINDOW_WIDTH  = 300
WINDOW_HEIGHT = 300

# This controls the pause time (in millisecond) for the animation
DELAY = 10


def main():
	window = Gwindow()
	rect = set_up_rect()
	window.add(rect)

	# animation
	vx = 5
	rect.move(vx, 0)
	while True:
		rect.move(vx, 0)
		if rect.x <= 0 or rect.x + SIZE >= WINDOW_WIDTH:
			vx = -vx
			if vx < 0:
				rect.filled = True
				rect.fill_color = 'blueviolet'
				rect.color = 'blueviolet'
			else:
				rect.filled = True
				rect.fill_color = 'dodgerblue'
				rect.color = 'dodgerblue'
		pause(10)


def set_up_rect():
	cx = (WINDOW_WIDTH-SIZE)/2
	cy = (WINDOW_HEIGHT-SIZE)/2
	rect = GRect(SIZE, SIZE, x=cx, y=cy)
	rect.filled = True
	rect.fill_color = 'dodgerblue'
	return rect


def Gwindow():
	return GWindow(width=WINDOW_HEIGHT, height=WINDOW_HEIGHT, title='bouncing_rect')

if __name__ == '__main__':
	main()
