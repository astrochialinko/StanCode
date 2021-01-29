"""
File: complement.py
Name: Chia-Lin Ko
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program asks uses for a DNA sequence,
    and finds the complement strand of a DNA sequence
    """
    # input the dna
    dna = str(input('Please give me a DNA strand and I\'ll find the complement: '))
    # check the input format
    while not is_dna(dna):
        print('Illegal format')
        dna = str(input('Please give me a DNA strand (A, T, C, G only) and I\'ll find the complement: '))

    # find the complement strand
    ans = build_complement(dna)
    print('The complement of ' + str(dna.upper()) + ' is ' + str(ans))


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


def build_complement(dna):
    """
    purpose:
        find the complement strand of a DNA sequence

    :param  dna: str, a DNA sequence
    :return ans: str, the complement strand of a DNA sequence
    """
    ans = ''
    # case-insensitive
    dna = dna.upper()
    # complement strand of a DNA sequence: A-T, G-C
    for dna_seg in dna:
        if dna_seg == 'A':
            ans += 'T'
        elif dna_seg == 'T':
            ans += 'A'
        elif dna_seg == 'G':
            ans += 'C'
        elif dna_seg == 'C':
            ans += 'G'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
