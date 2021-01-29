from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Chia-Lin Ko
----------------------------
This program instructs Karel to draw a checkerboard using 
beepers, as described in Assignment 1. 
The program works for all of the sample worlds provided in 
the starter folder.
"""


def main():
    """
    purpose:
        This program instructs Karel to draw a checkerboard using
        beepers, as described in Assignment 1.
    pre-condition:
        Karel is at (1,1), facing East
    post-condition:
        Karel is at (1,N), facing North
        (or at (1,1), facing West, if only one avenue. But facing North for 1x1).
        N is the total number of Street (last Street).
    """
    fill_one_line_with_spatial_arrangement()
    # facing East
    back_to_left()
    # facing North
    while front_is_clear():
        if not on_beeper():
            move()
            turn_right()
            # facing East
        else:
            move()
            if right_is_clear():
                turn_right()
                move()
                # facing East
            else:
                move()
                # facing North (for the case of one avenue only)
        fill_one_line_with_spatial_arrangement()
        # facing East (or North, if only one avenue)
        back_to_left()
        # facing North (or West, if only one avenue)

def fill_one_line_with_spatial_arrangement():
    """
    purpose:
        Karel will fill up a line with spatial arrangement
        as described in Assignment 1.
    pre-condition:
        Karel is at the beginning of the line, facing East (or North, if only one avenue).
    post-condition:
        Karel is at the end of the line, facing East (or North, if only one avenue) .
    """
    # facing East or North (if only one avenue)
    put_beeper()
    while front_is_clear():
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            put_beeper()


def back_to_left():
    """
     pre-condition:
         Karel is at the end of the line, facing East (or North, if only one avenue)
     post-condition:
         Karel is at the beginning of the line, facing North (or West, if only one avenue)
     """
    turn_around()
    # facing West (or South, if only one avenue)
    while front_is_clear():
        move()
    turn_right()
    # facing North (or East, if only one avenue)


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
