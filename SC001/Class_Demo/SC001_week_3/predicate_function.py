"""
File: predicate_function.py
Name: Jerry Liao 2020/08
-------------------------------
This program introduces a predicate function
, def is_odd(n), which returns True on odd
numbers and False on even numbers
"""


def main():
    """
    This program tells users if the input number is odd or not
    """
    print("This program tells you if 'a' is an odd number.")
    a = int(input('a: '))
    print(is_odd(a))


def is_odd(n):
    """
    :param n: int
    :return: bool, if n is an odd number or not
    """
    return n % 2 == 1


if __name__ == '__main__':
    main()
