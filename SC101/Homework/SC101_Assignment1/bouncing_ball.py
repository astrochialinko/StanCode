"""
File: bouncing_ball.py
Name: Chia-Lin Ko
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
click_num = 0
ball_x = START_X
ball_y = START_Y


window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # set up the initial ball
    ball = setup_ball()
    onmouseclicked(bouncing_ball)


def setup_ball():
    """
    This function sets the initial condition of the ball
    """
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)
    return ball


def bouncing_ball(mouse):
    """
    This function display the bouncing ball

    :param mouse:
    """
    global click_num, ball_x, ball_y

    # remove the initial ball
    ball_remove = window.get_object_at(START_X+SIZE/2, START_Y)
    window.remove(ball_remove)

    # the initial condition of the ball when clicking the mouse
    if ball_x == START_X:
        ball = setup_ball()
        vy = 0
    # no response for clicking the mouse when the ball is bouncing
    else:
        return None

    # move the ball
    while click_num < 3:
        if ball_x > WINDOW_WIDTH:
            click_num +=1
            ball_x = START_X
            ball = setup_ball()
            break
        else:
            ball.move(VX, vy)
            ball_x += VX
            # ball is falling
            if ball.y < (WINDOW_HEIGHT-SIZE):
                vy += GRAVITY
            # ball is bouncing
            else:
                if vy > 0:
                    vy = -vy * REDUCE
                else:
                    vy = vy * REDUCE
        pause(DELAY)


if __name__ == "__main__":
    main()
