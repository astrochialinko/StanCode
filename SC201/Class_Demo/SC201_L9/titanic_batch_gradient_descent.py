"""
File: titanic_batch_gradient_descent.py
Name: Chia-Lin Ko
-----------------------------
This file demonstrates how to use batch
gradient descent to update weights by numpy 
array. The training process should be way
faster than stochastic gradient descent
(You should see a smooth training curve as well)
-----------------------------
w1.shape = (n, 1)
X.shape = (n, m)
H.shape = (1, m)
Y.shape = (1, m)
"""


import time
import numpy as np


TRAIN = 'titanic_data/train.csv'
NUM_EPOCHS = 60000
ALPHA = 0.05


def main():
	start = time.time()
	X_train, Y = data_preprocessing()
	print('Y.shape', Y.shape)
	print('X.shape', X_train.shape)
	# ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
	n, m = X_train.shape
	X = normalize(X_train)

	# classifier = h.fit(X,Y)
	w, b = batch_gradient_descent(X, Y)
	
	# Predict
	# [-3.875, +4.33, +0.34, -1.44, ..., +10.33]
	scores = np.dot(w.T, X) + b	
	# sol 1
	predictions = np.where(scores>0, 1, 0)

	# sol 2
	# probability = 1/(1+np.exp(scores))
	# #                      condtion, True value, False value
	# predictions = np.where(probability>0.5, 1, 0)

	# sol 3, using for loop
	# predictions = []
	# for i in range(m):
	# 	if scores[0][i] > 0:
	# 		predictions.append(1)
	# 	else:
	# 		predictions.append(0)

	# accuracy
	# sol 1, 
	acc = np.equal(Y, predictions)	
	
	# sol 2, using for loop
	# acc = 0
	# for i in range(m):
	# 	if predictions[0][i] == Y[0][i]:
	# 		acc + 1

	print('--------------acc-----------------')
	print('Acc: ', np.sum(acc)/m)
	print('-----------------------------------')

	end = time.time()
	print('Total run time (Batch-GD):', end-start)


def normalize(X):
	"""
	:param X: numpy_array, the dimension is (n, m)
	:return: numpy_array, the values are normalized, where the dimension is still (n, m)
	"""
	# n -> Pclass, Sex, Age, Sibsp, Parch, Fare
	n, m = X.shape

	# sol 1
	max_over_m_data = np.max(X, axis=1, keepdims=True)
	min_over_m_data = np.min(X, axis=1, keepdims=True)
	X = np.divide(X-min_over_m_data, max_over_m_data-min_over_m_data)

	# sol 2, using for loop
	# for i in range(n):
	# 	max_over_m_data = np.max(X[i]) #   X[i].shape == (1, m)
	# 	min_over_m_data = np.min(X[i]) #
	# 	X[i] = (X[i]-min_over_m_data)/(max_over_m_data-min_over_m_data)
	return X



def batch_gradient_descent(X, Y):
	"""
	:param X: numpy_array, the array holding all the training data
	:param Y: numpy_array, the array holding all the ture labels in X
	:return: numpy_array, the trained weights with dimension (n, m)
	"""
	n, m = X.shape
	# Initialize w and b
	w = np.random.rand(n, 1)
	b = np.random.random()


	# Start Training
	for epoch in range(NUM_EPOCHS):
		# forwardProp
		K = w.T.dot(X) + b
		H = 1/(1+np.exp(-K))
		L = -(Y*np.log(H)+(1-Y)*np.log(1-H))
		J = (1/m)*np.sum(L)
		if epoch%1000 == 0:
			print('Cost: ', J)
		# backProp
		# w = w - ALPHA * dw
		w = w - ALPHA * ((1/m)*np.sum(X.dot((H-Y).T), axis=1, keepdims=True))
		# b = b - ALPHA * db
		b = b - ALPHA * ((1/m)*np.sum(H-Y))
	return w, b



def data_preprocessing(mode='train'):
	"""
	:param mode: str, indicating if it's training mode or testing mode
	:return: Tuple(numpy_array, numpy_array), the first one is X, the other one is Y
	"""
	data_lst = []
	label_lst = []
	first_data = True
	if mode == 'train':
		with open(TRAIN, 'r') as f:
			for line in f:
				data = line.split(',')
				# ['0PassengerId', '1Survived', '2Pclass', '3Last Name', '4First Name', '5Sex', '6Age', '7SibSp', '8Parch', '9Ticket', '10Fare', '11Cabin', '12Embarked']
				if first_data:
					first_data = False
					continue
				if not data[6]:
					continue
				label = [int(data[1])]
				if data[5] == 'male':
					sex = 1
				else:
					sex = 0
				# ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
				passenger_lst = [int(data[2]), sex, float(data[6]), int(data[7]), int(data[8]), float(data[10])]
				data_lst.append(passenger_lst) # List of lists
				label_lst.append(label) # list of int
	else:
		pass
	       # (m, 1).T            #(m, 1).T
	return np.array(data_lst).T, np.array(label_lst).T


if __name__ == '__main__':
	main()
