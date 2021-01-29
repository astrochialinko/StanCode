from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Chia-Lin Ko
--------------------------------
This program instructs Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    purpose:
        This program instructs Karel to fill up all the pillars
        with beepers.
    pre-condition:
        Karel is at (1,1), facing East
    post-condition:
        Karel is at (N,1), facing East.
        N is the total number of avenue (last avenue).
    """
    while front_is_clear():
        fill_pillar_with_beepers()
        back_to_bottom_from_top()
        if front_is_clear():
            go_to_next_pillar()
        if not front_is_clear():
            fill_pillar_with_beepers()
            back_to_bottom_from_top()


def fill_pillar_with_beepers():
    """
    purpose:
        Karel will fill up a pillar with beepers.
    pre-condition:
        Karel is at the bottom of the pillar, facing East
    post-condition:
        Karel is at the top of the pillar, facing North
    """
    turn_left()
    # facing North
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
    if not on_beeper():
        put_beeper()


def back_to_bottom_from_top():
    """
    purpose:
        Karel will move to the bottom of the pillar
        from the top of the pillar.
    pre-condition:
        Karel is at the top of the pillar, facing North
    post-condition:
        Karel is at the bottom of the pillar, facing East
    """
    turn_around()
    # facing South
    while front_is_clear():
        move()
    turn_left()
    # facing East


def go_to_next_pillar():
    """
    pre-condition:
        Karel is at (n,1), facing East
    post-condition:
        Karel is at (n+4,1), facing East
    """
    for i in range(4):
        move()


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
