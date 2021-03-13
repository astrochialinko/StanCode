"""
File: basic_permutations.py
Name: Chia-Lin Ko
-----------------------------
This program finds all the 3-digits binary permutations
by calling a recursive function binary_permutations.
Students will find a helper function useful in advanced
recursion problems.
"""


def main():
	binary_permutations(3)


def binary_permutations(n):
	binary_permutations_helper(n, '')


def binary_permutations_helper(n, current_digits):
	if len(current_digits) == n:
		print(current_digits)
	else:
		binary_permutations_helper(n, current_digits+'0')
		binary_permutations_helper(n, current_digits+'1')


if __name__ == '__main__':
	main()