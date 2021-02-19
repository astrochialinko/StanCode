"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3

# global variable
lives = NUM_LIVES
graphics = BreakoutGraphics()


def main():
    """
    This program displays the Breakout game
    """
    global lives, graphics

    # Add animation loop here!
    while True:

        # End of the Game
        if (lives == 0) or (graphics.brick_num == 0):
            break

        # Lose a life when the ball falls beyond the bottom edge
        if graphics.ball.y >= graphics.window.height:

            lives -= 1
            graphics.reset_ball()

        # Check for collision
        ball_ul = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        ball_ur = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        ball_bl = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        ball_br = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,
                                                graphics.ball.y+graphics.ball.height)

        # Reflection Setting: bricks and paddle
        if ball_ul is not None:
            reflection(ball_ul)
        elif ball_ur is not None:
            reflection(ball_ur)
        elif ball_bl is not None:
            reflection(ball_bl)
        elif ball_br is not None:
            reflection(ball_br)

        # Reflection Setting: walls
        if (graphics.ball.x <= 0) or (graphics.ball.x + graphics.ball.width >= graphics.window.width):
            graphics.reflect_ball_x()
        if graphics.ball.y <= 0:
            graphics.reflect_ball_y()

        # Animation: move the ball
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)

        # Pause
        pause(FRAME_RATE)


def reflection(ball):
    """
    purpose:
        This function will either (1) reflect the ball from the bricks and remove the bricks
        or (2) reflect the ball from the paddle

    :param ball: window.get_object_at(ball position)
    """

    global graphics
    # remove the bricks and reflect the ball from the bricks
    if ball != graphics.paddle:
        graphics.window.remove(ball)
        graphics.brick_num -= 1
        graphics.reflect_ball_y()
    # reflect the ball from the paddle
    else:
        dy = graphics.get_dy()
        if dy > 0:
            graphics.reflect_ball_y()


if __name__ == '__main__':
    main()
