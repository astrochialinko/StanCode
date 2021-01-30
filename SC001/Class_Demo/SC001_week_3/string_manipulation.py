"""
File: string_manipulation.py
Name: 
----------------------------
The goal of this file is to change
stancode to stanCode and show you
how to do string manipulations by
the following 3 steps:
(1) Start with an empty str
(2) Loop over the str
(3) Concatenation
"""


def main():
	s = 'stancode'
	ans=''
	for i in range(len(s)):
		ch = s[i]
		if ch == 'c':
			ans+='C' # switch
		else:
			ans+=ch # keep
	print(ans)

##### DO NOT EDIT THE CODE BELOW THIS LINE #####
if __name__ == '__main__':
	main()
