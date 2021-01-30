"""
File: stack_frame_error.py
Jerry Liao 2020/08
------------------------
This file shows the concept of parameter passing
through stack frames
"""


def main():
    """
    This program prints the value of a
    on Console. Is it 0 or 1?
    """
    print('-------------')
    a = 0
    plus_one(a)
    print(a)
    print('-------------')


def plus_one(a):
    """
    :param a: the number that is to be incremented
    """
    a += 1


if __name__ == '__main__':
    main()
