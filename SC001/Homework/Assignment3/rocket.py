"""
File: rocket.py
Name: Chia-Lin Ko
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This program draws ASCII art - a rocket.
	"""
	head(SIZE)
	belt(SIZE)
	upper(SIZE)
	lower(SIZE)
	belt(SIZE)
	head(SIZE)


def head(size):
	"""
	purpose:
		print the head of the rocket

	:param size: int, the size of the rocket
	"""
	for row in range(size):
		# space
		for i in range(size-row):
			print(' ', end="")
		# slash
		for i in range(row+1):
			print('/', end="")
		# backslash
		for i in range(row+1):
			print('\\', end="")

		# new line
		print('')


def belt(size):
	"""
	purpose:
		print the belt of the rocket

	:param size: int, the size of the rocket
	"""
	print('+', end="")
	for i in range(size):
		for j in range(2):
			print('=', end="")
	print('+')


def upper(size):
	"""
	purpose:
		print the upper of the rocket

	:param size: int, the size of the rocket
	"""
	for row in range(size):
		print('|', end="")
		# dot
		for i in range(size-row-1):
			print('.', end="")
		# slash & backslash
		for i in range(row+1):
			print('/', end="")
			print('\\', end="")
		# dot
		for i in range(size-row-1):
			print('.', end="")
		print('|', end="")

		# new line
		print('')


def lower(size):
	"""
	purpose:
		print the upper of the rocket

	:param size: int, the size of the rocket
	"""
	for row in range(size):
		print('|', end="")
		# dot
		for i in range(row):
			print('.', end="")
		# slash & backslash
		for i in range(size-row):
			print('\\', end="")
			print('/', end="")
		# dot
		for i in range(row):
			print('.', end="")
		print('|', end="")

		# new line
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()