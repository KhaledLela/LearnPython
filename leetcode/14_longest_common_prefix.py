"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix
https://github.com/KhaledLela/LearnPython/blob/main/leetcode/longest_common_prefix.py

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix,
return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from unittest import TestCase


class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""
        common_prefix = ""
        word = strs[0]
        for i in range(len(word)):
            char = word[i]
            for j in range(1, len(strs)):
                cw = strs[j]
                if len(cw) <= i or char != cw[i]:
                    return common_prefix
            common_prefix += char

        return common_prefix


class TestSol(TestCase):
    def test_romanToInt(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"

        # strs = ["dog", "racecar", "car"]
        # expected = ""

        self.assertEqual(Solution().longestCommonPrefix(strs), expected)
