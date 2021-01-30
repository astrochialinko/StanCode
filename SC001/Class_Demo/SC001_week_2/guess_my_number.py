"""
File: guess_my_number.py
Name:
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
import numpy as np
SECRET = int(np.random.random_sample()*100)
#SECRET = 0


def main():
    print('Guess a number from 0-99')
    while True:
        guess = int(input('Your guess: '))
        if guess < SECRET:
            print ('Too low')
        elif guess == SECRET:
            break
        else:
            print ('Too high')
    print('Congrats! The secret is ' + str(SECRET))


    # other solution
    # guess = int(input('Your guess: '))
    # while guess != SECRET:
    #     if guess > SECRET:
    #         print ('Too big')
    #     else:
    #         print ('Too small')
    #     guess = int(input('Your guess: '))
    # print ('Congrats! The secret is ' + str(SECRET))



### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
