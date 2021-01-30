"""
File: stack_frame_fixed.py
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
    a = plus_one(a)
    print(a)
    print('-------------')


def plus_one(a):
    """
    :param a: int, the number to be incremented
    :return a: int, the number that is 1 bigger than a
    """
    a += 1
    return a


if __name__ == '__main__':
    main()
