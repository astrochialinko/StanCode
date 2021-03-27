"""
File: anagram.py
Name: Chia-Lin Ko
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dictionary = []


def main():
    read_dictionary(FILE)
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        input_word = str(input("Find anagrams for: "))
        if input_word == '-1':
            break
        else:
            print('Searching...')
            found_list = find_anagrams(input_word)
            print('%d anagrams: '%(len(found_list)), end='')
            print(found_list)


def read_dictionary(FILE):
    with open(FILE, 'r') as f:
        for line in f:
            vocabulary = line.split('\n')[0].strip()
            dictionary.append(vocabulary)


def find_anagrams(s):
    """
    :param s: str, the input string
    :return found_list: list, list of found anagram(s)
    """
    found_list = []
    helper(s, '', found_list)
    return found_list


def helper(str, current_str, found_list):
    if (len(current_str) == len(str)) and (current_str in dictionary):
        print('Found: %s'%(current_str))
        found_list.append(current_str)
        print("Searching...")
    else:
        for i in range(len(str)):
            ele = str[i]
            ele_num_in_current_str = current_str.count(ele)
            ele_num_in_str = str.count(ele)
            if (ele_num_in_current_str < ele_num_in_str) and ((current_str+ele) not in found_list):
                if has_prefix(current_str):
                    # Choose
                    current_str += ele
                    # Explore
                    helper(str, current_str, found_list)
                    # Un-choose
                    current_str = current_str[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, the sub segment
    :return: bool, Ture if sub_s is a prefix of any one of the vocabulary in the dictionary
    """
    for dict_word in dictionary:
        if dict_word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
