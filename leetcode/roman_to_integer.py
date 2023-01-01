"""
https://leetcode.com/problems/roman-to-integer/
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


def romanToInt(s: str) -> int:
        cd = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        ac = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in cd:
                ac += cd[s[i:i + 2]]
                i += 2
            else:
                ac += cd[s[i]]
                i += 1
        return ac


class TestSol(TestCase):
    def test_romanToInt(self):
        actual = romanToInt("MCMXCIV")
        expected = 1994
        self.assertEqual(actual, expected)
