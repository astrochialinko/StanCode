"""
File: hailstone.py
Name: Chia-Lin Ko
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program simulates the execution of the Hailstone sequence,
    lists all the progress, and prints the number of steps (to reach 1).
    """
    print('This program compute Hailstone sequence.\n')
    data = int(input('Enter a number: '))
    # check if the input number is a positive integer
    while data < 1:
        data = int(input('Enter a positive integer: '))
    step = 0
    # start the Hailstone sequence
    while True:
        if data == 1:
            print('It took ' + str(step) + ' step(s) to reach 1.')
            break
        else:
            # even case
            if data%2 == 0:
                data_temp = int(data/2)
                print(str(data) + ' is even, so I take half: ' + str(data_temp))
                data = data_temp
            # odd case
            else:
                data_temp = 3*data + 1
                print(str(data) + ' is odd, so I make 3n+1: ' + str(data_temp))
                data = data_temp
            step+=1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
