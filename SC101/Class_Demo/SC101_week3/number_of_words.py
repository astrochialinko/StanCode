"""
File: number_of_words.py
Name: Chia-Lin Ko
-------------------------------
This file calculates the number of words in
romeojuliet.txt by using word.split() and
basic Python list operations
"""

FILE = 'romeojuliet.txt'


def main():

    # open the file
    with open(FILE, 'r') as f:
        count = 0

        for line in f:
            word_list = line.split()
            count += len(word_list)

    print(count)


if __name__ == '__main__':
    main()

