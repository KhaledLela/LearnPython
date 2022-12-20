"""
https://leetcode.com/problems/palindrome-number/
"""


def Palindrome():
    n = input('Enter a string or number:\n')
    if n == n[::-1]:
        print('This is a palindrome!')
    else:
        print('Not a palindrome!')


Palindrome()
