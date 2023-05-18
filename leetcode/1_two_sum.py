"""
1. Two Sum
https://leetcode.com/problems/two-sum
https://youtu.be/3nUkKzm2eW8
https://github.com/KhaledLela/LearnPython/blob/main/leetcode/two_sum.py

# Write a function takes list & target number
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

# Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10ˆ4
-10ˆ9 <= nums[i] <= 10ˆ9
-10ˆ9 <= target <= 10ˆ9
Only one valid answer exists.
"""

# @see unit_4_ex1.py for simple solution.
# O(n2)


# [11, 2, 7, 15]  target = nums[i] +
def twoSum(nums: [int], target: int) -> [int]:
    for i in range(len(nums)):  # O(n) nums[i] = 11
        for j in range(i + 1, len(nums)):  # O(n) nums[j] = 7
            if nums[i] + nums[j] == target:  # O(1)
                return [i, j]


# O(n)
# def twoSumEhanced(nums: [int], target: int) -> [int]:
#     seen_indexed_map = {}
#     for i in range(len(nums)):  # O(n)
#         val = nums[i]
#         com = target - val
#         if com in seen_indexed_map:  # O(1)
#             return [i, seen_indexed_map[com]]
#         seen_indexed_map[val] = i


print(twoSum([11, 2, 7, 15], 9))
