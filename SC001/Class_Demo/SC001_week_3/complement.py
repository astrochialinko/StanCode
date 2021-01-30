"""
File: complement.py
Name: Chia-Lin Ko
-----------------------
This file should define a console program that prompts a user for
a strand of DNA and displays the complement of that strand of DNA.
Further details and output format can be found in the Assignment 3
handout.
"""


def build_complement(dna):
    ans=''

    # case insensitive
    dna = dna.upper()

    # build complement
    for base in dna:
        if base == 'A':
            ans+= 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


def main():
    dna = input('your DNA:')
    print(build_complement(dna))

# ----- DO NOT EDIT THE CODE BELOW THIS LINE ----- #
if __name__ == "__main__":
    main()
