"""
File: hangman.py
Name: Chia-Lin Ko
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game
    """
    # initial condition
    ans = random_word()
    remaining_guess_num = N_TURNS
    guess_word = ''
    for i in range(len(ans)):
        guess_word += '-'

    # start to play hangman game
    while (remaining_guess_num > 0) and (guess_word != ans):
        print('The word looks like: ' + str(guess_word))
        print('You have ' + str(remaining_guess_num) + ' guesses left.')
        input_ch = str(input('Your guess: '))

        # illegal format
        if not input_ch.isalpha():
            print('illegal format.')
        elif len(input_ch) != 1:
            print('illegal format.')
        # correct format
        else:
            # case-insensitive
            input_ch = input_ch.upper()
            # wrong guess
            if ans.find(input_ch) == -1:
                print('There is no ' + str(input_ch) + '\'s in the word.')
                remaining_guess_num -= 1
            # correct guess
            else:
                print('You are correct!')
                ans_slice = ans
                # replace all the correct guessed letter(s)
                while ans_slice.find(input_ch) != -1:
                    replace_loc = len(ans) - len(ans_slice) + ans_slice.find(input_ch)
                    guess_word  = replace_letter(input_ch, replace_loc, guess_word)
                    ans_slice   = ans_slice[ans_slice.find(input_ch)+1:]
    # win
    if guess_word == ans:
        print('You win!!')
    # lose
    else:
        print('You are completely hung : (')
    print('The word was: ' + str(ans))


def replace_letter(letter, location, word):
    """
    purpose:
        Replace the letter in a word

    :param         letter: int, the replacing letter
    :param       location: int, the location of the replacing letter in the original word
    :param           word: int, the original word
    :return replaced_word: int, the replaced word
    """
    replaced_word = ''
    for i in range(len(word)):
        if i == location:
            replaced_word += letter
        else:
            replaced_word += word[i]
    return replaced_word


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
