"""
File: average_grades.py
Name: Chia-Lin Ko
-------------------------
This file stores all the scores
in a python list and calculates the
average of all elements in it
"""

# Constant
EXIT = -1  # Controls when to break the loop of score input


def main():
	"""
	This program asks inputs from users 
	"""
	print(f"This program averages the input(s), or {EXIT} to exit")
	
	lst = []
	# TODO: Add values to lst
	while True:
		score = int(input('Your score: '))

		if score == EXIT:
			break
		else:
			lst.append(score)
			# lst += [score]  different ways to append the score the the list
	
	print('The average:', average_by_index(lst))
	print('The average:', average_by_for_each(lst))


def average_by_index(scores):
	"""
	:param scores: (list) Containing all the scores input by user
	:return : (float) The average of the elements in scores
	----------------------------------------------
	This function uses indices in for loop to calculate
	the average of scores
	"""
	total = 0
	for i in range(len(scores)):
		score = scores[i]
		total += score

	return total/len(scores)


def average_by_for_each(scores):
	"""
	:param scores: (list) Containing all the scores input by user
	:return : (float) The average of the elements in scores
	----------------------------------------------
	This function uses for each loop to calculate
	the average of scores
	"""
	total = 0
	for score in scores:
		total += score

	return total/len(scores)


if __name__ == '__main__':
	main()
