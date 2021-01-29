from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Chia-Lin Ko
----------------------------
This program instructs Karel to leave a beeper on the corner closest 
to the center of 1st Street (or either of the two central corners if 
1st Street has an even number of corners).  
"""


def main():
    """
    purpose:
        This program instructs Karel to leave a beeper on the corner closest
        to the center of 1st Street.
    pre-condition:
        Karel is at (1, 1), facing East
    post-condition:
        Karel is at (N/2, 1) or (N/2+1, 1).
        N is the total number of Street(s).
    """
    if not front_is_clear():
        # Case 1: only one avenue
        put_beeper()
    else:
        move()
        if not front_is_clear():
            # Case 2: two avenues
            put_beeper()
        else:
            # Case 3: more than three avenues
            fill_one_line()
            # remove the edged (far right) beeper
            turn_around()
            pick_beeper()
            move()
            # remove the remaining edged beepers until the remaining center beeper
            while on_beeper():
                # check if the front step have beeper (not the center beeper)
                move()
                if on_beeper():
                    pick_beeper_to_next_grid_point()
                    go_to_edged_beeper()
            # back to the center beeper
            turn_around()
            move()
            # pick up all the beeper
            while on_beeper():
                pick_beeper()
            put_beeper()


def pick_beeper_to_next_grid_point():
    """
    pre-condition:
        Karel is at the grid point that the beeper will be moved to, facing center
    post-condition:
        Karel is at the edge of the line, facing center
    """
    turn_around()
    move()
    turn_around()
    # at the grid point that the beeper will be picked, facing center
    # start to move beeper(s)
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        turn_around()
        # facing edge
        move()
        turn_around()
        # at the grid point that the beeper will be picked, facing center


def go_to_edged_beeper():
    """
    pre-condition:
        Karel is at the grid point next to (one step outside) the edge (far East or far West)
        of the line that having beeper(s), facing center
    post-condition:
        Karel is at the edge (far West or far East)
        of the line that having beeper(s), facing center
    """
    move()
    # at the edge (far East or fat West) of the line that having beeper(s), facing center
    while on_beeper():
        move()
    # facing toward the edge
    turn_around()
    move()
    # facing toward the center

def fill_one_line():
    """
    pre-condition:
        Karel is at the fat left of the line, facing East
    post-condition:
        Karel is at the far right of the line, facing East
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def back_to_left():
    """
    pre-condition:
        Karel is at the far right of the line, facing East
    post-condition:
        Karel is at the fat left of the line, facing East
    """
    turn_around()
    # facing South
    while front_is_clear():
        move()
    turn_around()


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
