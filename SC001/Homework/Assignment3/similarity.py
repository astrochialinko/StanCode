"""
File: similarity.py
Name: Chia-Lin Ko
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program finds the best match of a short DNA sequence from a long DNA sequence
    """
    # input the dna
    long_dna = str(input('Please give me a DNA sequence to search: '))
    # check the input format
    while not is_dna(long_dna):
        print('Illegal format')
        long_dna = str(input('Please give me a DNA sequence (A, T, C, G only) to search: '))

    short_dna = str(input('What DNA sequence would you like to match? '))
    # check the input format
    while not is_dna(short_dna):
        print('Illegal format')
        short_dna = str(input('What DNA sequence (A, T, C, G only) would you like to match? '))

    # find the similarity
    ans = homology(long_dna, short_dna)
    print('The best match is ' + str(ans))


def is_dna(dna):
    """
    purpose:
        check if the format of input dna strand is correct

    :param   dna:  str, input dna strand
    :return bool: bool, Ture if the format is correct
    """
    # case-insensitive
    dna = dna.upper()
    # check the format
    for dna_seg in dna:
        if dna_seg not in ['A', 'T', 'G', 'C']:
            return False
    return True


def homology(whole, seg):
    """
    purpose:
        This program compares short dna sequence (short_sequence)
        with sub sequences of a long dna sequence (long_sequence)
        and return the best match of DNA

    :param whole: str, the whole DNA sequence
    :param   seg: str, the segment of whole DNA sequence
    :return  ans: str, the best match of DNA sequence
    """
    ans = ''
    max_match_num = 0
    # case-insensitive
    whole = whole.upper()
    seg = seg.upper()

    # check the similarity of whole sequence
    for i in range(len(whole)-len(seg)+1):
        check_seg = whole[i:i+len(seg)]
        match_num = 0

        # check the similarity of each check_seg
        for j in range(len(check_seg)):
            if check_seg[j] == seg[j]:
                match_num += 1

        # save the best match of check_seg
        if match_num > max_match_num:
            max_match_num = match_num
            ans = check_seg
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
