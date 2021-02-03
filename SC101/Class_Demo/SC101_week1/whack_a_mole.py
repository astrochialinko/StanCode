"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

# Constant controls the pause time of the animation
DELAY = 550

# Global variables
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title ='whack_a_mole')
score = 0
score_label = GLabel('Score: ' + str(score))

def main():
    onmouseclicked(remove_mole)
    score_label.font = '-30'
    window.add(score_label, 0, score_label.height)
    while True:
        img = GImage('mole.jpeg')
        random_x = random.randint(0, WINDOW_WIDTH - img.width)
        random_y = random.randint(0, WINDOW_HEIGHT - img.height)
        window.add(img, random_x, random_y)
        pause(DELAY)


def remove_mole(mouse):
    global score # tell the python that score is a global variable
    maybe_move = window.get_object_at(mouse.x, mouse.y)
    if (maybe_move is not None) and (maybe_move is not score_label):
        window.remove(maybe_move)
        score += 1
        score_label.text = 'Score: ' + str(score)


if __name__ == '__main__':
    main()
