"""
File: draw_line.py
Name: Chia-Lin Ko
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
start_x, start_y = 0, 0
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='draw_line.py')


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
    global click_num, start_x, start_y

    if click_num % 2 == 0:
        # draw a circle
        start_x = mouse.x - SIZE / 2
        start_y = mouse.y - SIZE / 2
        circle = GOval(SIZE, SIZE, x=start_x, y=start_y)
        window.add(circle)
    else:
        # remove the circle
        circle_remove = window.get_object_at(start_x+SIZE/2, start_y)
        window.remove(circle_remove)

        # draw a Line
        end_x = mouse.x
        end_y = mouse.y
        line = GLine(start_x+SIZE/2, start_y+SIZE/2, end_x, end_y)
        window.add(line)
    click_num += 1


if __name__ == "__main__":
    main()
