"""
File: cabin_preprocess.py
Name: Jerry Liao
------------------------------------
This file shows how to pre-process cabin data in titanic_data/train.csv.
2 main tasks to do in this file:
  - Cleaning missing data
  - Making data into a one-hot vector (because the data is not correlated)
"""


def main():
    """
    Cleaning missing data in titanic_data/train.csv and making it a one-hot vector
    """
    cabin_list = cabin_preprocess('titanic_data/train.csv')
    cabin_list = sorted(cabin_list)
    print(cabin_list)
    cabin_encoding = encoding(cabin_list)
    print(cabin_encoding)


def cabin_preprocess(filename):
    """
    :param filename: str, the file to be processed
    """
    cabin_names = []
    with open(filename, 'r') as f:
        target_i = -1
        first = True
        for line in f:
            lst = line.split(',')
            if first:
                for i in range(len(lst)):
                    if 'Cabin' == lst[i]:
                        target_i = i + 1      # Name has 2 components
                first = False
            else:
                name = lst[target_i]
                if name not in cabin_names:
                    cabin_names.append(name)
    return cabin_names


def encoding(lst):
    """
    : param lst: list, the Python list containing all the cabin names
    """
    d = {}
    for i in range(len(lst)):
        d[lst[i]] = i
    return d


if __name__ == '__main__':
    main()