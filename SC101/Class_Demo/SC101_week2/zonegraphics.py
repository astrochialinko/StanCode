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

        self.dx = 0
        self.dy = 0
        self.lives = 3
        self.reset_ball()

        # Lives Word
        self.lives_word = GLabel('Lives: ' + str(self.lives), x=WINDOW_WIDTH * 0.02, y=WINDOW_HEIGHT * 0.1)
        self.lives_word.font = 'Courier-25-bold'
        self.w.add(self.lives_word)

        # Initialize mouse listeners
        onmouseclicked(self.handle_click)

    def handle_click(self, event):
        obj = self.w.get_object_at(event.x, event.y)
        if obj == self.ball:
            self.reset_ball()

    def reset_ball(self):
        self.set_ball_position()
        while self.ball_in_zone():
            self.set_ball_position()
        self.set_ball_velocity()
        self.w.add(self.ball)

    def set_ball_position(self):
        self.ball.x = random.randint(0, self.w.width-self.ball.width)
        self.ball.y = random.randint(0, self.w.height-self.ball.height)

    def ball_in_zone(self):
        zone_left_side = self.zone.x
        zone_right_side = self.zone.x + self.zone.width
        is_ball_x_in_zone = (zone_left_side-self.ball.width) <= self.ball.x <= zone_right_side

        zone_top = self.zone.y
        zone_bottom = self.zone.y + self.zone.height
        is_ball_y_in_zone = (zone_top-self.ball.height) <= self.ball.y <= zone_bottom

        return (is_ball_x_in_zone and is_ball_y_in_zone)

    def set_ball_velocity(self):
        self.dx = random.randint(0, MAX_SPEED)
        self.dy = random.randint(MIN_Y_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx
        if random.random() > 0.5:
            self.dy = -self.dy