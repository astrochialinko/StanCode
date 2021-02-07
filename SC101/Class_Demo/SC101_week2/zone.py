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
    graphics = ZoneGraphics()
    while True:
        # Update
        graphics.ball.move(graphics.vx, graphics.vy)

        # Check
        if (graphics.ball.x < 0) or (graphics.ball.x+graphics.ball.width > graphics.w.width):
            graphics.vx = -1*graphics.vx
        if (graphics.ball.y < 0) or (graphics.ball.y+graphics.ball.height > graphics.w.height):
            graphics.vy = -1*graphics.vy

        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
