"""
File: replace_keyword.py
Name:
----------------------
This file shows how to replace
old_word with new_word by the function called replace
"""


def main():
	s = replace('Jerry hates coding', 'hates', 'teaches')
	print(s)


def replace(old_s, old_word, new_word):
	if old_word not in old_s:
		return 'go away!'
	else:
		ans=''
		# the words before old_word
		i = old_s.find(old_word)
		ans += old_s[:i]

		# changed word
		ans+= new_word

		# the words after new_word
		ans+= old_s[i+len(old_word):]

		return ans

if __name__ == '__main__':
	main()
