#!/usr/local/anaconda3/envs/stanCode37/bin/python3
"""
File: interactive.py
Name: Chia-Lin Ko
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
# although this movie suffers from some cliche , this film is still worth watching
"""
from util import *
from submission import *

def main():

    weight_fn = './weights'
    weights = {}
    with open(weight_fn, 'r') as f:
        lines = f.readlines()
        for line in lines:
            key = str(line.split()[0].strip())
            value = float(line.split()[1].strip())
            weights[key] = value
    interactivePrompt(extractWordFeatures, weights)


if __name__ == '__main__':
    main()