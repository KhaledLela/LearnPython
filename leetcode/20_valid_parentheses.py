"""
https://leetcode.com/problems/valid-parentheses
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
from unittest import TestCase


class Solution:

    def isValid(self, s: str) -> bool:
        #     if s is None or len(s) == 0 or len(s) % 2 != 0: return False
        #     parentheses = ('()', '[]', '{}')
        #     closed = (')', ']', '}')
        #     parts = []
        #     for char in s:
        #         # if nested and char not in closed: return False
        #         if char in closed and len(parts) == 0: return False
        #         if char in closed:
        #             pair = parts.pop() + char
        #             if pair not in parentheses: return False
        #         else:
        #             parts.append(char)
        #     return not parts

        if s is None or len(s) == 0 or len(s) % 2 != 0: return False
        brackets = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char: return False
        return not stack


class TestSol(TestCase):
    def test_valid_parentheses(self):
        s = '()'
        expected = True

        s = '()[]{}'
        expected = True

        s = '(([]){})'
        expected = True
        self.assertEqual(Solution().isValid(s), expected)
