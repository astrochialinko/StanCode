#!/usr/local/anaconda3/envs/stanCode37/bin/python3
"""
File: validEmailAddress.py
Name: Chia-Lin Ko
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: 0.65385
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data(DATA_FILE)
	is_email_lst = [0 for _ in range(13)] + [1 for _ in range(13)] # invalid(13) + valid(13), 0/1 for invalid/valid
	is_correct_lst = [0] * len(maybe_email_list) # 0/1 for wrong/correct
	
	for ind, maybe_email in enumerate(maybe_email_list): 
		feature_vector = feature_extractor(maybe_email)
		score = sum(feature_vector[i]* WEIGHT[i][0] for i in range(len(WEIGHT)))

		# calculate accuracy
		if (is_email_lst[ind] and score>0) or (not is_email_lst[ind] and score<0): 
			is_correct_lst[ind] = 1
	accuracy = sum(is_correct_lst)/len(is_correct_lst)
	print('Accuracy of this model: %.5f'%(accuracy))


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):

		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
			if feature_vector[i]:
				before_at, after_at = maybe_email.split('@', 1)
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' not in before_at else 0
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if before_at else 0
		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if after_at else 0
		elif i == 4:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in after_at else 0
		elif i == 5:
			feature_vector[i] = 1 if ' ' not in maybe_email else 0
		elif i == 6:
			feature_vector[i] = 1 if maybe_email[-4:] == '.com' else 0
		elif i == 7:
			feature_vector[i] = 1 if maybe_email[-4:] == '.edu' else 0
		elif i == 8:
			feature_vector[i] = 1 if maybe_email[-3:] == '.tw' else 0
		elif i == 9:
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0

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
