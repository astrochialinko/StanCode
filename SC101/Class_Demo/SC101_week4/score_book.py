"""
File: score_book.py
Name: Chia-Lin Ko
----------------------
This program shows all the 
dict method by implementing 
a score book.
"""

# This controls when to break the loop for user inputs
QUIT = ''


def main():
	"""
	This main method contains 3 methods that
	constructing a score book. d is passed by reference
	"""
	d = {}
	get_scores(d)
	check_score(d)
	print_scores(d)
	

def get_scores(d):
	"""
	: param d: (dict) an empty python dict 
	--------------------------------------
	This method puts key->value pairs in d
	"""
	print("Let's input some data!")

	while True:
		name = input("Name: ")
		if name == QUIT:
			break
		score = int(input('Score: '))
		d[name] = score


def check_score(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This checks if key in d
	"""
	print("Let's check the score!")
	while True:
		check_name = input('The name you want to check: ')
		if check_name == QUIT:
			break
		if check_name in d:
			the_score = d[check_name]
			print('Score: '+ str(the_score))
		else:
			print(f'There is no {check_name} in it.')


def print_scores(d):
	"""
	: param d: (dict) a python dict contains name->score
	--------------------------------------
	This method prints out all the key-value pairs
	"""
	print('-----------------------')
	for student_name, student_score in d.items():
		print(student_name, '->', student_score)


if __name__ == '__main__':
	main()