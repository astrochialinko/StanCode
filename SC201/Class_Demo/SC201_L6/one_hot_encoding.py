"""
File: one_hot_encoding.py
Name: 
---------------------------
This file shows how to pandas and sklearn
packages to build a machine learning project
from scratch by their high order abstraction.
The steps of this project are:
1) Data pre-processing by pandas (use one-hot encoding technique!)
2) Learning by sklearn
3) Test on D_test
"""

import pandas as pd
from sklearn import linear_model, preprocessing


# Constants - filenames for data set
TRAIN_FILE = 'titanic_data/train.csv'                         # Training set filename
TEST_FILE = 'titanic_data/test.csv'                           # Test set filename

# Global Variable   
cache = {}                                                    # Cache for test set


def main():
	"""
	The only part that is different from the 'titanic_pandas.py'
	is the one_hot_encoding part. 
	"""

	# Training set pre-processing
	train_data = data_preprocess(TRAIN_FILE, mode='Train')
	labels = train_data.Survived

	# Test set pre-processing
	test_data = data_preprocess(TEST_FILE, mode='Test')

	# Training set pre-processing
	train_data.pop('PassengerId')
	train_data.pop('Survived')
	train_data.pop('Name')
	train_data.pop('Ticket')

	# Test set pre-processing
	test_data.pop('PassengerId')
	test_data.pop('Name')
	test_data.pop('Ticket')

	#############################
	# Degree 2 Polynomial Model #
	#############################

	# Data Preprocessing
	poly_feature_extractor = preprocessing.PolynomialFeatures(degree=2)
	x_train_poly = poly_feature_extractor.fit_transform(train_data)
	standardizer = preprocessing.StandardScaler()
	x_train_poly = standardizer.fit_transform(x_train_poly)

	# Training
	h = linear_model.LogisticRegression(max_iter=10000)
	classifier_poly = h.fit(x_train_poly, labels)

	# Accuracy
	print(classifier_poly.score(x_train_poly, labels))

	# Test
	x_test_poly = poly_feature_extractor.transform(test_data)
	x_test_poly = standardizer.transform(x_test_poly)
	predictions = classifier_poly.predict(x_test_poly)
	test(predictions)


def data_preprocess(filename, mode='Train'):
	"""
	:param filename: str, the file to read in
	:param mode: str, indicating if it's training mode or testing mode
	"""

	# A column based DataFrame
	data = pd.read_csv(filename)
	if mode == 'Train':
		# Cleaning the missing data in Fare column by replacing NaN with its median
		fare_median = data['Fare'].dropna().median()
		data['Fare'] = data['Fare'].fillna(fare_median)

		# Cleaning the missing data in Age column by replacing NaN with its median
		age_median = data['Age'].dropna().median()
		data['Age'] = data['Age'].fillna(age_median)

		# Cache some data for test set
		cache['Fare'] = fare_median
		cache['Age'] = age_median
	else:
		data['Fare'] = data['Fare'].fillna(cache['Fare'])
		data['Age'] = data['Age'].fillna(cache['Age'])

	# Changing 'male' to 1, 'female' to 0
	data.loc[data.Sex == 'male', 'Sex'] = 1
	data.loc[data.Sex == 'female', 'Sex'] = 0

	# Changing 'S' to 0, 'C' to 1, 'Q' to 2
	data['Embarked'] = data['Embarked'].fillna('S')
	data.loc[data.Embarked == 'S', 'Embarked'] = 0
	data.loc[data.Embarked == 'C', 'Embarked'] = 1
	data.loc[data.Embarked == 'Q', 'Embarked'] = 2

	# Make more sense for Sex and Embarked!
	data = one_hot_encoding(data, mode)

	return data


def one_hot_encoding(data, mode):
	"""
	:param data: pd.DataFrame, the 2D data 
	:param mode: str, indicating if it's Train for Test
	"""
	# One hot encoding for a new category Male

	# One hot encoding for a new category Female

	# No need Sex anymore!

	# One hot encoding for a new category FirstClass

	# One hot encoding for a new category SecondClass

	# One hot encoding for a new category ThirdClass

	# No need Pclass anymore!

	# One hot encoding for each cabin

	return data


def test(results):
	"""
	: param predictions: numpy.array, a list-like data structure that stores 0's and 1's
	: param filename: str, the filename you would like to write the results to
	"""
	print('\n==========================')
	filename = 'my_pandas_submission.csv'
	print('Writing results to ...')
	print(filename)
	with open(filename, 'w') as out:
		out.write('PassengerId,Survived\n')
		start_id = 892
		for ans in results:
			out.write(str(start_id)+','+str(ans)+'\n')
			start_id += 1
	print('\n==========================')


if __name__ == '__main__':
	main()
