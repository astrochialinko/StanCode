"""
File: largest_digit.py
Name: Chia-Lin Ko
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the input integers
	:return: int, the biggest digit in the input integers
	"""
	if n < 0:
		n = -n
	units_digit = n%10
	tens_digit  = (n//10)%10

	if tens_digit == 0:
		return n
	elif tens_digit >= units_digit:
		return find_largest_digit(n//10)
	else:
		return find_largest_digit(n//10 - tens_digit + units_digit)


if __name__ == '__main__':
	main()
