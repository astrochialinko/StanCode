#!/usr/bin/env python3

"""
Stanford CS106AP
TK Drawing Lecture Exercises
Courtesy of Nick Parlante
"""

import tkinter as tk


# provided function, this code is complete
def make_canvas(width, height):
    """
    Creates and returns a drawing canvas
    of the given int size, ready for drawing.
    """
    top = tk.Tk()
    top.minsize(width=width + 10, height=height + 10)

    canvas = tk.Canvas(top, width=width, height=height)
    canvas.pack()
    canvas.xview_scroll(6, "units")  # hack so (0, 0) works correctly
    canvas.yview_scroll(6, "units")

    return canvas


def main():
    w = make_canvas(500, 300)
    w.create_text(0, 0, text='stanCode', anchor=tk.NW, fill='red')
    w.create_line(0, 300, 300, 300, width=10, fill='blue')
    tk.mainloop()
    

if __name__ == '__main__':
    main()
