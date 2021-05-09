"""
File: titanic_survived.py
Name: Chia-Lin Ko
----------------------------------
This file contains 3 of the most important steps
in machine learning:
1) Data pre-processing
2) Training
3) Predicting
"""
import math

TRAIN_DATA_PATH = 'titanic_data/train.csv'
NUM_EPOCHS = 1000
ALPHA = 0.01


def sigmoid(k):
    """
    :param k: float, linear function value
    :return: float, probability of the linear function value
    """
    return 1/(1+math.exp(-k))


def dot(lst1, lst2):
    """
    : param lst1: list, the feature vector
    : param lst2: list, the weights
    : return: float, the dot product of 2 list
    """
    return sum(lst1[i]*lst2[i] for i in range(len(lst1)))


def main():
    # Milestone 1
    training_data = data_pre_processing()

    # ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    weights = [0]*len(training_data[0][0])

    # Milestone 2
    training(training_data, weights)

    # Milestone 3
    predict(training_data, weights)


# Milestone 1
def data_pre_processing():
    """
    Read the training data from TRAIN_DATA_PATH and get ready for training!
    :return: list[Tuple(data, label)], the value of each data on
    (['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'], 'Survived')
    """
    with open(TRAIN_DATA_PATH, 'r') as f:
        is_first = True
        training_data = []
        for line in f:
            if is_first:
                is_first = False
            else:
                feature_vector, label = feature_extractor(line)
                training_data.append((feature_vector, label))
                
    return training_data


def feature_extractor(line):
    """
    : param line: str, the line of data extracted from the training set
    : return: list, the feature vector
    """
    
    data_list = line.split(',')
    feature_vector = []
    label = int(data_list[1])

    # ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    for i in range(len(data_list)):
        if i == 2:
            # Pclass
            feature_vector.append((int(data_list[i])-1)/2)
        elif i == 5:
            # Gender
            if data_list[i] == 'male':
                feature_vector.append(0)
            else:
                feature_vector.append(1)
        elif i == 6:
            # Age
            if data_list[i].isdigit():
                feature_vector.append((float(data_list[i])-0.42)/(80-0.42))
            else:
                feature_vector.append((29.699-0.42)/(80-0.42)) # average age
        elif i == 7:
            # SibSp
            feature_vector.append((int(data_list[i])-0)/(8-0))
        elif i == 8:
            # Parch
            feature_vector.append((int(data_list[i])-0/(6-0)))
        elif i == 10:
            # Fare
            feature_vector.append((float(data_list[i])-0)/(512.33-0))
        elif i == 12:
            # Embarked
            if data_list[i] == 'C':
                feature_vector.append((0-0)/2)
            elif data_list[i] == 'Q':
                feature_vector.append((2-0)/2)
            else: # S and missing value
                feature_vector.append((1-0)/2) 
            
    return (feature_vector, label)


# Milestone 2
def training(training_data, weights):
    """
    : param training_data: list[Tuple(data, label)], the value of each data on
    (['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'], 'Survived')
    : param weights: list[float], the weight vector (the parameters on each feature)
    """
    for epoch in range(NUM_EPOCHS):
        cost = 0
        for x, y in training_data:
            #################################

            h = sigmoid(dot(x, weights))
            cost += -(y*math.log(h)+(1-y)*math.log(1-h))

            # w = w - alpha * dL_dw
            # wi = wi - alpha * (h-y)*xi
            for i in range(len(x)):
                weights[i] = weights[i] - ALPHA * (h-y) * x[i]
            #################################
        cost /= (2*len(x))
        if epoch%100 == 0:
            print('Cost over all data:', cost)


# Milestone 3
def predict(training_data, weights):
    """
    : param training_data: list[Tuple(data, label)], the value of each data on
    (['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'], 'Survived')
    : param weights: list[float], the weight vector (the parameters on each feature)
    """
    acc = 0
    num_data = 0
    for x, y in training_data:
        predict = get_prediction(x, weights)
        print('True Label: ' + str(y) + ' --------> Predict: ' + str(predict))
        if y == predict:
            acc += 1
        num_data += 1
    print('---------------------------')
    print('Acc: ' + str(acc / num_data))


def get_prediction(x, weights):
    """
    : param x: list[float], the value of each data on
    ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    : param weights: list[float], the weight vector (the parameters on each feature)
    : return: float, the score of x (if it is > 0 then the passenger may survive)
    """
    k = dot(x, weights)
    h = sigmoid(k)
    if h > 0.5:
        return 1
    else:
        return 0
    '''
    # other solution
    if k > 0:
        return 1
    else:
        return 0
    '''

if __name__ == '__main__':
    main()
