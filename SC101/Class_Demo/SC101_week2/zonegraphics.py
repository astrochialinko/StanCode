from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.w = GWindow(width=window_width, height=window_height, title='Zone_Game')

        # Create zone
        self.zone = GRect(zone_width, zone_height, x=(self.w.width-zone_width)/2, y=(self.w.height-zone_height)/2)
        self.zone.color = 'blue'
        self.w.add(self.zone)

        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True

        self.set_ball_position()
        self.w.add(self.ball)

        self.vx = random.randint(0, MAX_SPEED)
        self.vy = random.randint(MIN_Y_SPEED, MAX_SPEED)

        # Score word
        self.score_word = GLabel('Score: ', x= WINDOW_WIDTH*0.02, y=WINDOW_HEIGHT*0.1)
        self.score_word.font = 'Courier-25-bold'
        self.w.add(self.score_word)

        # Initialize mouse listeners
        #onmouseclicked(restart)

    def set_ball_position(self):
        while True:
            rand_x = random.randint(0, self.w.width  - self.ball.width)
            rand_y = random.randint(0, self.w.height - self.ball.height)
            if (self.zone.x > rand_x or self.zone.x + self.zone.width < rand_x) or \
               (self.zone.y > rand_y or self.zone.y + self.zone.height < rand_y):
                break

        self.ball.x = rand_x
        self.ball.y = rand_y