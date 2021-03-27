"""
File: boggle.py
Name: Chia-Lin Ko
----------------------------------------
This program display the boggle game
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROW_NUM = 4
COLUMN_NUM = 4

# Global variable
dictionary = []


def main():
	read_dictionary(FILE, voc_lower_length=4)

	# set the boggle
	boggle = []
	for row in range(ROW_NUM):
		while True:
			letters = input("%s row of letters: "%(row+1))
			boggle.append([])
			wrong_format = False
			for column in range(COLUMN_NUM):
				letter = letters.split()[column]
				if letter.isalpha() and len(letter)==1:
					boggle[row].append(letter.lower())
				else:
					wrong_format = True
					print('Illegal input')
					boggle.pop()
					break

			if not wrong_format:
				break

	# test
	# boggle = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]

	# start the boggle
	found_list = find_letter(boggle)
	print('There are %d words in total.'%(len(found_list)))


def find_letter(boggle):
	# convert the 2d list to 1d list
	boggle_1d = list_2dto1d(boggle)
	found_list = []
	ini_raw = [i for i in range(len(boggle))]
	ini_column = [i for i in range(len(boggle[0]))]
	for i in ini_raw:
		for j in ini_column:
			helper(boggle_1d, '', i, j, [], found_list)
	return found_list


def helper(boggle_1d, current_str, last_row, last_column, chosen_order, found_list):

	if (current_str in dictionary) and (current_str not in found_list):
		print('Found "%s"' % (current_str))
		found_list.append(current_str)

	for i in range(len(boggle_1d)):
		order = i
		row, column, letter = boggle_1d[i]
		if  (-1 <= (int(row)    - int(last_row))    <= 1) and\
			(-1 <= (int(column) - int(last_column)) <= 1) and\
			(order not in chosen_order):
			if has_prefix(current_str+letter):
				# choose
				current_str += letter
				chosen_order.append(order)
				# Explore
				helper(boggle_1d, current_str, row, column, chosen_order, found_list)
				# Un-choose
				current_str = current_str[:-1]
				chosen_order.pop()


def list_2dto1d(list_2d):
	# convert the 2d list to 1d list, including the row and column info.
	list_1d = []
	for i in range(len(list_2d)):
		for j in range(len(list_2d[0])):
			# row, column, element
			list_1d.append((i, j, list_2d[i][j]))
	return list_1d


def read_dictionary(FILE, voc_lower_length=1):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			vocabulary = line.split('\n')[0].strip()
			if len(vocabulary) >= voc_lower_length:
				dictionary.append(vocabulary)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for dict_word in dictionary:
		if dict_word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
