"""
File: bouncing_ball.py
Name: TA
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
CLICK_NUM_LIMIT = 3
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# Global variable
count = 0
lock = True

window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # set up the initial ball
    setup_ball()
    onmouseclicked(bouncing_ball)


def setup_ball():
    """
    This function sets the initial condition of the ball
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)


def bouncing_ball(mouse):
    """
    This function simulates the bouncing process

    :param mouse:
    """
    global count, lock

    # the initial condition of the ball when clicking the mouse
    vy = 0

    if lock and count <=3:
        lock = False  # used to close the mouse-clicked function

        # move the ball
        while True:
            ball.move(VX, vy)
            pause(DELAY)

            # ball is falling
            vy += GRAVITY

            # ball is outside of the window
            if ball.x > window.width:
                count += 1
                setup_ball()
                lock = True  # used to open the mouse-clicked function
                break

            # ball is bouncing
            if ball.y > (window.height-SIZE) and vy >0:
                vy *= -REDUCE


if __name__ == "__main__":
    main()
