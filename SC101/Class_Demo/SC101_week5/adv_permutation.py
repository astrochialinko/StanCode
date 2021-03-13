"""
File: adv_permutation.py
Name: Chia-Lin Ko
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	permutation_helper(lst, [])


def permutation_helper(lst, current_list):
	if len(current_list) == len(lst):
		print(current_list)
	else:
		for ele in lst:
			if ele not in current_list:
				# Choose
				current_list.append(ele)
				# Explore
				permutation_helper(lst, current_list)
				# Un-choose
				current_list.pop()


if __name__ == '__main__':
	main()