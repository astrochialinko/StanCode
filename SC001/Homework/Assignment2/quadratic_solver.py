"""
File: quadratic_solver.py
Name: Chia-Lin Ko
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program asks 3 inputs (a, b, and c) from users
	to compute the roots of equation:
	ax^2 + bx + c = 0.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	# print the number and value(s) of the real root(s)
	quadratic_solver(a, b, c)


def quadratic_solver(a, b, c):
	"""
	This function aims to find (and print out) the real root(s) of a quadratic equation.

	:param a: float, the coefficients of x^2 of a quadratic equation
	:param b: float, the coefficients of x of a quadratic equation
	:param c: float, the constant of a quadratic equation
	:return: str, the number and the value(s) (if any) of the real solution(s)
	"""
	discriminant = b*b - 4*a*c
	# case 1: no real roots (complex solutions)
	if discriminant < 0:
		print('No real roots')
	# case 2: one real root
	elif discriminant == 0:
		solve1 = (-1 * b + math.sqrt(discriminant)) / (2 * a)
		print('One root: ' + str(solve1))
	# case 3: two real roots
	else:
		solve1 = (-1 * b + math.sqrt(discriminant)) / (2 * a)
		solve2 = (-1 * b - math.sqrt(discriminant)) / (2 * a)
		print('Two roots: ' + str(solve1) + ' , ' + str(solve2))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
