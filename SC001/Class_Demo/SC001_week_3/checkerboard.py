"""
File: checkerboard.py
Name: Chia-Lin Ko
------------------------
This program prints an alternating 
checkerboard pattern on Console
by using nested for loop.
"""

# These constants control the diameter of the checkerboard
ROW = 5  # The number of rows
COL = 8  # The number of cols


def main():

	# print checkerboard
	for i in range(ROW):
		for j in range(COL):
			if (i+j)%2 == 0:
				print('A', end='')
			else:
				print('*', end='')
		print('')



####  DO NOT EDIT CODE BELOW THIS LINE  ####
if __name__ == '__main__':
	main()