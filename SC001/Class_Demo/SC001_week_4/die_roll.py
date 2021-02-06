"""
File: die_roll.py
Name: Chia-Lin Ko
---------------------
This file uses random to simulate
4 dice roll for shi-ba-la
"""

import random

# This constant controls the number of players for the game
NUM_PLAYER = 5

# This constant shows the number of dice for shi-ba-la
NUM_DICE = 4


def main():
    """
    This program uses random to simulate real dice roll for shi-ba-la
    """

    for i in range(NUM_PLAYER):
        while True:
            rolls = ''
            for j in range(NUM_DICE):
                roll = random.randrange(0, 7)
                rolls += str(roll)
            if all_the_same(rolls) or two_the_same(rolls):
                break
        print(rolls)


# def two_the_same(str):
#     for str_pos in range(len(str)):
#         for i in range(str_pos):
#             str_seg = str[str_pos]
#             if str_seg == str[i]:
#                 print(str_seg, str[i])


def two_the_same(rolls):
    for i in range(len(rolls)):
        target = rolls[i]
        count = 0
        for j in range(len(rolls)):
            if i != j:
                if rolls[j] == target:
                    count += 1
        if count == 1:
            return True
    return False


def all_the_same(rolls):
    target = rolls[0]
    for i in range(1, len(rolls)):
        if rolls[i] != target:
            return False
    return True

if __name__ == '__main__':
    main()
