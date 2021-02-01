"""
File: my_drawing.py
Name: Chia-Lin Ko
----------------------
This program plots a heart and a rainbow to express "Love is love"
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow

# constant for window
WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 600
# constant for rainbow
RAINBOW_COLOR_LIST = ['#FFD2D2', '#FFEEDD', '#FFFFDF', '#DFFFDF', '#D2E9FF', '#F1E1FF', '#ececec']
# constant for heart
SIZE = 20  # 42
X_SCALE = 3 / WINDOW_WIDTH
Y_SCALE = -3 / WINDOW_HEIGHT
X_SHIFT = WINDOW_WIDTH / 2
Y_SHIFT = WINDOW_HEIGHT / 2 + 30
INTERVAL = 25  # 50
COLOR_LIST = ['red', 'darkorange', 'yellow', 'forestgreen', 'dodgerblue', 'darkviolet']


def main():
    """This program plots a heart and a rainbow to express 'Love is love' """
    find_maxmin()
    window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='LoveisLove.py')
    add_rainbow(window)
    add_heart(window)
    add_words(window)


def add_heart(window):
    """This function add a heart to the window"""

    # initial settings for plotting the heart
    y_max, y_min = 525, 85  # 520, 90
    y_interval = 70.83  # 71.6
    y_list = [y_min + i * y_interval for i in range(len(COLOR_LIST) + 1)]

    # start to draw a heart
    for y in range(0, WINDOW_HEIGHT, INTERVAL):
        for x in range(0, WINDOW_WIDTH, INTERVAL):
            # equation for heart
            cx = (x - X_SHIFT) * X_SCALE
            cy = (y - Y_SHIFT) * Y_SCALE
            love = ((cx**2 + cy**2 - 1) ** 3) - (cx**2 * cy**3)
            # plot the squares inside the heart
            if love < 0:
                for i in range(len(y_list)):
                    if i != len(y_list) - 1:
                        if y_list[i] < y <= y_list[i + 1]:
                            square = GRect(SIZE, SIZE, x=x-SIZE/2, y=y-SIZE/2)
                            square.filled = True
                            square.color = COLOR_LIST[i]
                            square.fill_color = COLOR_LIST[i]
                            window.add(square)


def add_rainbow(window):
    """This function add a rainbow to the window"""

    # initial setting for the rainbow
    size_ini_cir = 600
    x_cir = WINDOW_WIDTH * 0.5
    y_cir = WINDOW_HEIGHT * 0.85
    int_cir = 50

    # plot the concentric circles
    for i in range(len(RAINBOW_COLOR_LIST)):
        size_cir = size_ini_cir - int_cir * i
        circle = GOval(size_cir, size_cir, x=x_cir - size_cir / 2, y=y_cir - size_cir / 2)
        circle.filled = True
        circle.color = RAINBOW_COLOR_LIST[i]
        circle.fill_color = RAINBOW_COLOR_LIST[i]
        window.add(circle)

    # block the lower part of the circles by overlaying a box
    rect = GRect(size_ini_cir, size_ini_cir / 2, x=x_cir - size_ini_cir / 2, y=y_cir)
    rect.filled = True
    rect.color = RAINBOW_COLOR_LIST[-1]
    rect.fill_color = RAINBOW_COLOR_LIST[-1]
    window.add(rect)


def add_words(window):
    """This function add words to the window"""

    # plot the word1
    word1 = GLabel('LOVE', x=WINDOW_WIDTH * 0.3, y=WINDOW_HEIGHT * 0.45)
    word1.color = 'black'
    word1.font = 'Courier-100-bold'
    window.add(word1)

    # plot the word2
    word2 = GLabel('IS', x=WINDOW_WIDTH * 0.45, y=WINDOW_HEIGHT * 0.5)
    word2.color = 'black'
    word2.font = 'Courier-50-bold'
    window.add(word2)

    # plot the word3
    word3 = GLabel('LOVE', x=WINDOW_WIDTH * 0.3, y=WINDOW_HEIGHT * 0.65)
    word3.color = 'black'
    word3.font = 'Courier-100-bold'
    window.add(word3)


def find_maxmin():
    """
    This function find the maximum and minimum y values of squares inside the heats,
    and estimate the interval y value based on the length of the COLOR_LIST.
    """
    y_max, y_min = 0, WINDOW_HEIGHT

    # start to draw a heart
    for y in range(0, WINDOW_HEIGHT, INTERVAL):
        for x in range(0, WINDOW_WIDTH, INTERVAL):
            cx = (x - X_SHIFT) * X_SCALE
            cy = (y - Y_SHIFT) * Y_SCALE
            love = ((cx ** 2 + cy ** 2 - 1) ** 3) - (cx ** 2 * cy ** 3)
            if love < 0:
                # find_max
                if y > y_max:
                    y_max = y
                # find_min
                if y < y_min:
                    y_min = y

    y_interval = (y_max - y_min) / len(COLOR_LIST)
    print('y_max = %.2f, y_min = %.2f' % (y_max, y_min))
    print('y_interval = %.2f' %(y_interval))


if __name__ == '__main__':
    main()
