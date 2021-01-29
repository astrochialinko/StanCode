"""
File: caesar.py
Name: Chia-Lin Ko
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program demonstrates the idea of caesar cipher.
    """
    secret_num = int(input('Secret number: '))
    cipher = str(input('What\'s the ciphered string? '))

    ans = decipher(cipher, secret_num)
    print('The deciphered string is: ' + str(ans))


def decipher(cipher, secret_num):
    """
    purpose:
        Decipher the cipher by the given secret number

    :param     cipher: str, the input cipher
    :param secret_num: int, the secret number
    :return       ans: int, the deciphered string
    """

    # new_alphabet (given the input secret number)
    new_alphabet = ''
    for i in range(len(ALPHABET)):
        new_alphabet += ALPHABET[i-secret_num]

    # decipher
    ans = ''
    # case-insensitive
    cipher = cipher.upper()
    for i in range(len(cipher)):
        cipher_seg = cipher[i]
        if cipher_seg.isalpha():
            ans += ALPHABET[new_alphabet.find(cipher_seg)]
        else:
            ans += cipher_seg
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
