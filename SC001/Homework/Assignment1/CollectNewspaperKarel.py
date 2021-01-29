from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Chia-Lin Ko
--------------------------------
This program instructs Karel to walk to the door of its house, 
pick up the newspaper (represented by a beeper, of course), 
and then return to its initial position in the upper left corner 
of the house.
"""


def main():
    """
    purpose:
        Karel will move to the (6,3) from (3,4),
        pick up the newspaper (beeper),
        and bring the newspaper back to the initial position of (3,4).
    pre-condition:
        Karel is at (3,4), facing East.
    post-condition:
        Karel is at (3,4), facing East with the newspaper (beeper).
    """
    move_to_newspaper()
    bring_newspaper_home()


def move_to_newspaper():
    """
    purpose:
        Karel will move to the (6,3) from (3,4).
    pre-condition:
        Karel is at (3,4), facing East.
    post-condition:
        Karel is at (6,3), facing East.
    """
    turn_right()
    move()
    turn_left()
    # facing East
    move()
    move()
    move()


def bring_newspaper_home():
    """
    purpose:
        Karel will pick up the newspaper (beeper) and
        bring the newspaper back to the initial position of (3,4).
    pre-condition:
        Karel is at (6,3), facing East.
    post-condition:
        Karel is at (3,4), facing East with the newspaper (beeper).
    """
    pick_beeper()
    turn_around()
    # facing West
    move()
    move()
    move()
    turn_right()
    # facing North
    move()
    turn_right()
    put_beeper()
    # facing East


def turn_right():
    """
    This function turns Karel to the left 3 times.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    This function turns Karel to the left 2 times.
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
