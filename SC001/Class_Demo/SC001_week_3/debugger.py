"""
File: debugger.py
Name: Jerry Liao 2020/08
------------------------------
This program shows students how to use
PyCharm debugger to find bugs in their program.
It also emphasizes the concept of stack
frames between function calls
"""

import math


def main():
    test1 = mystery1()
    test1 /= 2
    test2 = mystery2(test1)
    test3 = mystery3(test2)
    test3 %= 2
    print(test3)


def mystery1():
    a = 53
    a -= 1
    return a%11


def mystery2(j):
    j += 1
    j += mystery1()
    k = math.sqrt(j)
    return k


def mystery3(k):
    k /= math.sqrt(0.09)
    k *= math.sin(-1.23)
    k -= 1
    k -= mystery1()
    return int(k)


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
