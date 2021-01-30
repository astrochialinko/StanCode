"""
File: reverse_string.py
Name: Jerry Liao 2020/08
----------------------------
The goal of this file is to 
reverse "stressed". You will 
see something cool ; )
"""


def main():
	"""
	This program reverses 'stressed'
	"""
	s = 'stressed'
	print(reverse(s))


def reverse(string):
	"""
	:param string: The word to be reversed
	:return result: The reversed string
	"""
	result = ''
	for i in range(len(string)):
		result = string[i] + result
	return result



##### DO NOT EDIT THE CODE BELOW THIS LINE #####
if __name__ == '__main__':
	main()
