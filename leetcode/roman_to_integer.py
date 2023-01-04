"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
https://youtu.be/GklNd06Za0w
https://github.com/KhaledLela/LearnPython/blob/main/leetcode/roman_to_integer.py
"""
from unittest import TestCase

"""
Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


# def romanToInt(s: str) -> int:
#     cd = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000,
#         'IV': 4,
#         'IX': 9,
#         'XL': 40,
#         'XC': 90,
#         'CD': 400,
#         'CM': 900,
#     }
#     ac = 0
#     i = 0
#     while i < len(s):
#         if i + 1 < len(s) and s[i:i + 2] in cd:
#             ac += cd[s[i:i + 2]]
#             i += 2
#         else:
#             ac += cd[s[i]]
#             i += 1
#     return ac


#
#
# def romanToInt(s: str) -> int:
#     cd = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     ac = 0
#     count = len(s)
#     for i in range(count):
#         cv = cd[s[i]]
#         if i + 1 < count and cv < cd[s[i + 1]]:
#             ac -= cv
#         else:
#             ac += cv
#     return ac


# Chat GPT: Here is a solution in Python:
# Explanation:
#
# We start by defining a dictionary that maps each Roman numeral to its corresponding integer value.
# Then, we initialize a result variable to 0.
# We iterate through the characters in the input string.
# For each character, we check if it has a larger value than the previous character.
# If it does, we subtract twice the value of the previous character to account for
# the fact that it was added in the previous step and then subtracted in this step.
# If the current character does not have a larger value than the previous character,
# we simply add its value to the result.
# At the end, we return the result.
# This solution should run in O(n) time, where n is the length of the input string.

def romanToInt(s: str) -> int:
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(s)):
        if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i - 1]]:
            result += roman_to_int[s[i]] - 2 * roman_to_int[s[i - 1]]
        else:
            result += roman_to_int[s[i]]
    return result


class TestSol(TestCase):
    def test_romanToInt(self):
        actual = romanToInt("MCMXCIV")
        expected = 1994
        self.assertEqual(actual, expected)
