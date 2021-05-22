#!/usr/local/anaconda3/envs/stanCode37/bin/python3

import math
import random
import numpy as np
from collections import defaultdict
from util import *
from typing import Any, Dict, Tuple, List, Callable

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]


############################################################
# Milestone 3a: feature extraction

def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    d = defaultdict(int)
    for word in x.split():
        d[word] += 1
    return d
    # END_YOUR_CODE


############################################################
# Milestone 4: Sentiment Classification
def sigmoid(k):
    return 1/(1+math.exp(-k))

def learnPredictor(trainExamples: List[Tuple[Any, int]], validationExamples: List[Tuple[Any, int]],
                   featureExtractor: Callable[[str], FeatureVector], numEpochs: int, alpha: float) -> WeightVector:
    """
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numEpochs|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement gradient descent.
    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and validationExamples
    to see how you're doing as you learn after each epoch. Note also that the 
    identity function may be used as the featureExtractor function during testing.
    """
    weights = {}  # feature => weight
    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    # error_arr = np.zeros((numEpochs, 3))
    for epoch in range(numEpochs):
        for i in range(len(trainExamples)):
            data, y = trainExamples[i]
            # y = 0 if int(label) == -1 else 1 # y=1/0 for positive/negative review
            featureVector = featureExtractor(data)
            # hinge = max(0, 1-h*y)
            # h = phi_x dot weights
            # hinge = max(0, 1-(phi dot w)y)
            if dotProduct(weights, featureVector)*y >= 1:
                # w = w -alpha * 0
                scale = 0
            else:
                # w = w - alpha * (-phi * y)
                scale = -(alpha) * (-y)
            increment(weights,scale,featureVector)

            # h = sigmoid(dotProduct(weights,featureVector))
            # increment(weights,-alpha*(h-y),featureVector)


        def predictor(x): return 1 if dotProduct(weights,featureExtractor(x)) > 0 else -1
        trainError = evaluatePredictor(trainExamples, predictor)
        validationError = evaluatePredictor(validationExamples, predictor)
        print('Training Error: (%s epoch): %s'%(epoch, trainError))
        print('Validation Error: (%s epoch): %s'%(epoch, validationError))
    #     error_arr[epoch][0] = epoch
    #     error_arr[epoch][1] = trainError
    #     error_arr[epoch][2] = validationError
    # np.savetxt('./Milestone1/error_word.txt', error_arr, header='Epoch Training_Error Validation_Error')

     # END_YOUR_CODE
    return weights


############################################################
# Milestone 5a: generate test case

def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    """
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    """
    random.seed(42)

    def generateExample() -> Tuple[Dict[str, int], int]:
        """
        Return a single example (phi(x), y).
        phi(x) should be a dict whose keys are a subset of the keys in weights
        and value is exactly 1.
        y should be 1 or -1 as classified by the weight vector.
        Note that the weight vector can be arbitrary during testing.
        """
        # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
        sub_weight = dict(random.sample(weights.items(), k=random.randint(1,len(weights))))
        phi = {key: 1 for key in sub_weight}
        y = 1 if dotProduct(phi, weights) >=0 else -1
        # END_YOUR_CODE
        return phi, y

    return [generateExample() for _ in range(numExamples)]


############################################################
# Milestone 5b: character features

def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    """
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    """

    def extract(x: str) -> Dict[str, int]:
        # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
        x = x.replace(" ", "")
        d = defaultdict(int)
        for i in range(len(x)-n+1):
            d[str(x[i:i+n])]+=1
        return d
        # END_YOUR_CODE

    return extract


############################################################
# Problem 3f: 
def testValuesOfN(n: int):
    """
    Use this code to test different values of n for extractCharacterFeatures
    This code is exclusively for testing.
    Your full written solution for this problem must be in sentiment.pdf.
    """
    trainExamples = readExamples('polarity.train')
    validationExamples = readExamples('polarity.dev')
    featureExtractor = extractCharacterFeatures(n)
    weights = learnPredictor(trainExamples, validationExamples, featureExtractor, numEpochs=20, alpha=0.01)
    outputWeights(weights, 'weights')
    outputErrorAnalysis(validationExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
    trainError = evaluatePredictor(trainExamples,
                                   lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    validationError = evaluatePredictor(validationExamples,
                                        lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    print(("Official: train error = %s, validation error = %s" % (trainError, validationError)))

