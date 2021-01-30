"""
File: how_many_lines.py
Name: Jerry Liao 2020/09
---------------------------
This file shows how to calculate
the number of lines in romeojuliet.txt
by Python code
"""

# This constant shows the file path to romeojuliet.txt
FILE = 'text/romeojuliet.txt'


def main():
	"""
	This program prints the number of
	lines in romeojuliet.txt on Console
	"""
	count = 0
	with open(FILE, 'r') as f:
		for line in f:
			count += 1
	print('There are ' + str(count) + ' lines in '+str(FILE))


if __name__ == '__main__':
	main()
