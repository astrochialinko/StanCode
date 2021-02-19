"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5   # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH   = 40  # Height of a brick (in pixels).
BRICK_HEIGHT  = 15  # Height of a brick (in pixels).
BRICK_ROWS    = 10  # Number of rows of bricks.
BRICK_COLS    = 10  # Number of columns of bricks.
BRICK_OFFSET  = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS   = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH  = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED     = 5    # Maximum initial horizontal speed for the ball.
BRICK_COL_LIST  = ['red', 'orange', 'yellow', 'green', 'blue']  # List for the brick color

# Global variable
unlock = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height,
                            x=self.window.width - paddle_width / 2,
                            y=self.window.height - paddle_offset
                            )
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2,
                          x=self.window.width / 2 - BALL_RADIUS,
                          y=self.window.height / 2 - BALL_RADIUS
                          )
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.move_ball)

        # Draw bricks.
        for yi in range(BRICK_ROWS):
            for xi in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT,
                                   x=xi * (BRICK_SPACING + BRICK_WIDTH),
                                   y=BRICK_OFFSET + yi * (BRICK_SPACING + BRICK_HEIGHT)
                                   )
                self.brick.filled = True
                self.brick.fill_color = BRICK_COL_LIST[yi // 2]
                self.brick.color = BRICK_COL_LIST[yi // 2]
                self.window.add(self.brick)
        # Number of bricks
        self.brick_num = BRICK_ROWS * BRICK_COLS

    def reflect_ball_x(self):
        self.__dx = -self.__dx

    def reflect_ball_y(self):
        self.__dy = -self.__dy

    def move_ball(self, event):
        """
        This function will move the ball when the user click the cursor,
        but will do nothing when the game is on.
        """
        global unlock
        if unlock:
            unlock = False
            # reset ball velocity
            self.set_ball_velocity()

    def reset_ball(self):
        """
        This program will reset the ball position and the ball velocity
        """
        global unlock
        # reset ball position
        self.ball.x = self.window.width / 2 - BALL_RADIUS
        self.ball.y = self.window.height / 2 - BALL_RADIUS
        # reset ball velocity
        self.__dx = 0
        self.__dy = 0
        unlock = True

    def move_paddle(self, mouse_move):
        """
        This function will control how the paddle move when the user moves the cursor
        """
        mouse_center = mouse_move.x - self.paddle.width / 2
        if mouse_center < (self.paddle.width / 2):
            self.paddle.x = 0
        elif mouse_center > (self.window.width - self.paddle.width / 2):
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse_center

    def set_ball_velocity(self):
        """
        This function sets the ball velocity
        """
        self.__dx = random.randrange(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Getter
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
