"""
File: find_max.py
Name:
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 2
in Assignment 2
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print('This program finds the maximum (or -1 to quit)')
    data = int(input('Your data:'))
    # This is the first data
    if data == EXIT:
        print('No Number')
    else:
        maximum = data
        while True:
            data = int(input('Value:'))
            if data == EXIT:
                break
            if data > maximum:
                maximum = data
        print(maximum)





### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
