"""
File: my_drawing.py
Name: Chia-Lin Ko
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GLabel, GObject, GPolygon
from campy.graphics.gwindow import GWindow
import numpy as np

WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 600

def main():
    window = GWindow(width=600, height=600, title='MyDrawing')

    dish = GOval(300, 300, x=150, y=100)
    window.add(dish)

    arc = myGArc(100, 100, 0, 90, x=100, y=100)
    window.add(arc)
    # print(arc.start_point)
    # print(arc.end_point)



    #arc.rotate()
    # arc2 = GArc(50, 50, 0, 180, x=0 ,y=0)
    # window.add(arc2)
    # print(arc2.start_point)
    # print(arc2.end_point)
    #
    # arc3 = GArc(50, 50, 0, 270, x=0, y=0)
    # window.add(arc3)
    # print(arc3.start_point)
    # print(arc3.end_point)
    #
    # arc4 = GArc(50, 100, 90, 180, x=50, y=50)
    # window.add(arc4)
    # print(arc4.start_point)
    # print(arc4.end_point)
    #
    # dish2 = GRect(width=100, height=100, x=50, y=50)
    # # dish2._transformed = True
    # # gobject_rotate(dish2, 30)
    # # dish2.transformed = True
    # dish2.rotate(90)
    # window.add(dish2)

    word = GLabel('Hello Word!', 50, 100)
    window.add(word)


    # a = GOval(200, 200, x=300, y=100)
    # a.filled = True
    # a.fill_color = 'red'
    # window.add(a)
    # b = GOval(200, 200, x=250, y=200)
    # b.filled = True
    # b.fill_color = 'green'
    # window.add(b)
    # c = GOval(200, 200, x=350, y=200)
    # c.filled = True
    # c.fill_color = '#003000'
    # window.add(c)


    # a = GRect(200, 200, x=200, y=100)
    # window.add(a)


def myGArc(width, height, start_ang, sweep_ang, x=0, y=0):
    rx, ry = width/2, height/2
    cx, cy = x+rx, y+ry

    angs = np.linspace(start_ang, sweep_ang, 10000)
    arc = GPolygon()
    for ang in angs:
        arc_x = cx + rx*np.cos(np.deg2rad(ang))
        arc_y = cy - ry*np.sin(np.deg2rad(ang))
        arc.add_vertex((arc_x, arc_y))
        #print(ang)
    # end_x = cx + rx*np.cos(np.deg2rad(start_ang+sweep_ang))
    # end_y = cy - ry*np.sin(np.deg2rad(start_ang+sweep_ang))

    return arc





if __name__ == '__main__':
    main()
