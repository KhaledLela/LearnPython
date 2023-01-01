"""
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [], l2: []):
        sum_nums = []
        r = 0

        for a, b in zip(l1, l2):
            print('{} {}'.format(a, b))


s = Solution()
s.addTwoNumbers([3, 4, 5], [3, 4, 5, 6])
