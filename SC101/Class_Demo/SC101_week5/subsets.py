"""
File: subsets.py
Name: Chia-Lin Ko
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    #list_sub_lists([1, 2, 3, 4])
    list_sub_lists(['a', 'b', 'c', 'd'])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    helper(lst, [])


def helper(lst, current):
    if len(lst) == 0:
        print(current)
    else:
        # Choose
        ele = lst.pop()
        # Explore w/o ele
        helper(lst, current)
        # Explore w/ ele
        current.append(ele)
        helper(lst, current)
        # Un-choose
        current.pop()
        lst.append(ele)

if __name__ == '__main__':
    main()
