"""
File: center_me.py
Name: Jerry Liao 2020/05
--------------------------------
This program shows how to center a GRect
on windows where the width and the height are
randomly chosen
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow

# It controls the width and height of the rect
SIZE = 100


def main():
    """
    Center a magenta rect on the canvas
    where the width and height are SIZE
    """
    rect = GRect(SIZE, SIZE)
    rect.filled = True
    rect.color = 'magenta'
    rect.fill_color = 'magenta'
    window = GWindow()
    rect_x = (window.width-rect.width)/2
    rect_y = (window.height-rect.height)/2
    window.add(rect, rect_x, rect_y)


if __name__ == '__main__':
    main()
