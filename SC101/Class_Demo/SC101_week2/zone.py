from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics(ball_radius=20)
    lives = NUM_LIVES

    while True:
        # Pause
        pause(FRAME_RATE)

        # check if hitting the zone
        if graphics.ball_in_zone():
            lives -= 1
            graphics.lives_word.text = ('Lives: ' + str(lives))
            if lives > 0:
                graphics.reset_ball()
            else:
                break

        # Animation
        graphics.ball.move(graphics.dx, graphics.dy)

        # Reflection Setting
        if (graphics.ball.x <=0) or (graphics.ball.x + graphics.ball.width >= graphics.w.width):
            graphics.dx = -graphics.dx
        if (graphics.ball.y <= 0) or (graphics.ball.y + graphics.ball.height >= graphics.w.height):
            graphics.dy = -graphics.dy


if __name__ == '__main__':
    main()
