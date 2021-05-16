"""
File: titanic_pandas.py
Name: 
---------------------------
This file shows how to pandas and sklearn
packages to build a machine learning project
from scratch by their high order abstraction.
The steps of this project are:
1) Data pre-processing by pandas
2) Learning by sklearn
3) Test on D_test
"""

import pandas as pd
from sklearn import linear_model, preprocessing


# Constants - filenames for data set
TRAIN_FILE = 'titanic_data/train.csv'                    # Training set filename
TEST_FILE = 'titanic_data/test.csv'                      # Test set filename

# Global variable
nan_cache = {}                                           # Cache for test set missing data


def main():

	# Data cleaning
	train_data = data_preprocess(TRAIN_FILE, mode='Train')
	test_data = data_preprocess(TEST_FILE, mode='Test')

	# Extract true labels
	

	# Extract features ('Pclass', 'Age', 'Sex', 'SibSp', 'Parch', 'Fare', 'Embarked')


	# Standardization
	

	# Degree 1 Polynomial


	# Test
	

def data_preprocess(filename, mode='Train'):
	"""
	: param filename: str, the csv file to be read into by pd
	: param mode: str, the indicator of training mode or testing mode
	-----------------------------------------------
	This function reads in data by pd, changing string data to float, 
	and finally tackling missing data showing as NaN on pandas
	"""

	# Read in data as a column based DataFrame

	if mode == 'Train':
		# Cleaning the missing data in Age column by replacing NaN with its median
		pass

		# Cache some data for test set
		

	else:
		# Fill in the NaN cells by the values in nan_cache to make it consistent
		pass

	# Changing 'male' to 1, 'female' to 0
	

	# Changing 'S' to 0, 'C' to 1, 'Q' to 2

	return None
	

def test(predictions, filename):
	"""
	: param predictions: numpy.array, a list-like data structure that stores 0's and 1's
	: param filename: str, the filename you would like to write the results to
	"""
	print('\n==========================')
	print('Writing predictions to ...')
	print(filename)
	with open(filename, 'w') as out:
		out.write('PassengerId,Survived\n')
		start_id = 892
		for ans in predictions:
			out.write(str(start_id)+','+str(ans)+'\n')
			start_id += 1
	print('\n==========================')


if __name__ == '__main__':
	main()
