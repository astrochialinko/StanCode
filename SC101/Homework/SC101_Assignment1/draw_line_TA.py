"""
File: draw_line.py
Name: TA
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the circle
SIZE = 10
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Global variable
click_num = 0
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='draw_line.py')
oval = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
       This function can draw a line.

       :param mouse:
    """
    global click_num

    click_num += 1
    if click_num % 2 == 1:
        window.add(oval, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
    else:
        line = GLine(oval.x+SIZE/2, oval.y+SIZE/2, mouse.x, mouse.y)
        window.add(line)
        window.remove(oval)


if __name__ == "__main__":
    main()
