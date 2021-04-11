#!/usr/local/anaconda3/envs/stanCode37/bin/python
"""
File: LC204_count_primes.py
Name: Chia-Lin Ko
Create Date: April 10, 2021
------------------------
LeetCode 204. Count Primes
Count the number of prime numbers less than a non-negative number, n.
"""
class Solution:

    def countPrimes(n: int) -> int:
        if n < 3:
            return 0
        else:
            # list begin with 2, n=i+2
            prime_lst = [True]*(n-2)
            for i in range(n-2):
                if prime_lst[i]:
                    prime_lst[(i+2)+i::i+2] =[False]*len(prime_lst[(i+2)+i::i+2])
            return sum(prime_lst)


def main():
    n = int(input('Input: '))
    prime_num = Solution.countPrimes(n)
    print('Output:', prime_num)

if __name__ == '__main__':
    main()