#!/usr/local/anaconda3/envs/stanCode37/bin/python3
"""
File: validEmailAddress_2.py
Name: Chia-Lin Ko
----------------------------
Please construct your own feature vectors
and try to surpass ~70% accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  No '@' in the str
feature2:  The '.', '-', '_' appear consecutively more than twice without without quoting (") 
feature3:  Before @, there is no alphabet or digit
feature4:  Before @, the '.', '-', '_' appear as the first or last character without quoting (")
feature5:  After @, there are alphabets
feature6:  After @, there is no '.' 
feature7:  After @, the words are end with '.org'
feature8:  After @, the words are end with '.com'
feature9:  After @, the words are end with '.edu'
feature10: After @, the words are end with '.tw'

Accuracy of this model: 0.92308
"""
import numpy as np
from collections import Counter

WEIGHT = np.array([               # The weight vector selected by you
	[-1],                          
	[-1],	
	[-1],
	[-1],
	[0.2],
	[-1],
	[0.2],
	[0.2],
	[0.2],
	[0.2]
])

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data(DATA_FILE)
	weight_vector = WEIGHT.T
	is_email_arr = np.zeros(len(maybe_email_list))
	is_email_arr[13:] = 1 # invalid(13) + valid(13), 0/1 for invalid/valid
	is_correct_arr = np.zeros(len(maybe_email_list)) # 0/1 for wrong/correct
	
	for ind, maybe_email in enumerate(maybe_email_list):
		feature_vector = feature_extractor(maybe_email)
		score = weight_vector.dot(feature_vector)
		
		# calculate accuracy
		if (is_email_arr[ind] and score>0) or (not is_email_arr[ind] and score<0): 
			is_correct_arr[ind] = 1
	print('Accuracy of this model: %.5f'%(np.mean(is_correct_arr)))


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = np.zeros((len(WEIGHT),1))
	for i in range(len(feature_vector)):
		special_str = ['.', '_', '-']
		quote_str = ['"', '“', '”']

		if i == 0:
			feature_vector[i][0] = 1 if '@' not in maybe_email else 0
			if not feature_vector[0][0]:
				before_at, after_at = maybe_email.split('@', 1)
		elif i == 1:
			if not any(s in quote_str for s in maybe_email): # no quote_str
				for s_ind, s in enumerate(maybe_email):
					pre_s = maybe_email[s_ind-1] if s_ind !=0 else ''
					if (s == pre_s) and (s in special_str): # special_str appears more than twice
						feature_vector[i][0] = 1
						break
		elif i == 2:
			if not feature_vector[0][0]:
				feature_vector[i][0] = 0 if any(s.isdigit() or s.isalpha() for s in before_at) else 1
			else: # no @
				feature_vector[i][0] = 1
		elif i == 3:
			if not feature_vector[0][0]:
				if before_at and (not any(s in quote_str for s in before_at)): # no quote_str
					if (before_at[0] in special_str) or (before_at[-1] in special_str):
						feature_vector[i][0] = 1
		elif i == 4:
			if not feature_vector[0][0]:
				feature_vector[i][0] = 1 if any(s.isalpha() for s in after_at) else 0
		elif i == 5:
			if not feature_vector[0][0]:
				feature_vector[i] = 1 if '.' not in after_at else 0
		elif i == 6:
			if not feature_vector[0][0]:
				feature_vector[i][0] = 1 if maybe_email[-4:] == '.org' else 0
		elif i == 7:
			if not feature_vector[0][0]:
				feature_vector[i][0] = 1 if maybe_email[-4:] == '.com' else 0
		elif i == 8:
			if not feature_vector[0][0]:
				feature_vector[i][0] = 1 if maybe_email[-4:] == '.edu' else 0
		elif i == 9:
			if not feature_vector[0][0]:
				feature_vector[i][0] = 1 if maybe_email[-3:] == '.tw' else 0
	return feature_vector


def read_in_data(filename):
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	lst = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			lst.append(line[:-1]) # remove the \n
	return lst


if __name__ == '__main__':
	main()
