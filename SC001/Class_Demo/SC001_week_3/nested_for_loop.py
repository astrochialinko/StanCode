"""
File: nested_for_loop.py
Name: Chia-Lin Ko
------------------------
This program show students the basic
concepts of nested (double) for loop
by printing a 4 rows 3 cols rectangle
"""

# These constants control the diameter of the rectangle
ROW = 4  # The number of rows
COL = 3  # The number of cols


def main():

	# # print #s
	# for i in range(ROW):
	# 	for j in range(COL):
	# 		print('#', end="")
	# 	print("")

	# # print #s
	# for i in range(3):
	# 	for j in range(i+1):
	# 		print('#', end="")
	# 	print("")

	# checker board
	for i in range(4):
		for j in range(4):
			if (i+j)%2==0:
				print('#', end="")
			else:
				print(' ', end="")
		print("")

####  DO NOT EDIT CODE BELOW THIS LINE  ####
if __name__ == '__main__':
	main()