"""
File: my_upper.py
Name: Chia-Lin Ko
----------------------
This file shows how python
built-in s.upper() is implemented
"""


def main():
	s = '123JeRrY123'
	print(upper(s))


def upper(s):
	ans=''
	for i in range(len(s)):
		ch = s[i]
		if ch.islower():
			ans+=ch.upper()
		else:
			ans+=ch
	return ans


if __name__ == '__main__':
	main()
