"""
File: dice_rolls_sum.py
Name: Chia-Lin Ko
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8


def main():
    dice_sum(TOTAL)


def dice_sum(target_sum):
    count_lst = [0]
    dice_sum_helper(target_sum, [], count_lst)
    print(count_lst[0])


def dice_sum_helper(target_sum, current, count_lst):
    if target_sum == sum(current):
        print('Yes:',current)
    else:
        print('N:',current)
        for roll in range(1, 7):
            count_lst[0] += 1
            if sum(current) < target_sum:
                # Choose
                current.append(roll)
                # Explore
                dice_sum_helper(target_sum, current, count_lst)
                # Un-choose
                current.pop()
            else:
                break


if __name__ == '__main__':
    main()
