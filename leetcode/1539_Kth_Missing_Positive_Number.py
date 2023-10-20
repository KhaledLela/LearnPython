"""
https://leetcode.com/problems/kth-missing-positive-number/

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Follow up:

Could you solve this problem in less than O(n) complexity?
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_arr = []
        for i in range(1, len(arr) + k + 1):
            if i not in arr:
                missing_arr.append(i)

            if len(missing_arr) == k:
                return missing_arr[k - 1]

    # def findKthPositive(self, arr, k):
    #     left, right = 0, len(arr) - 1
    #
    #     while left <= right:
    #         mid = left + (right - left) // 2
    #         missing_numbers = arr[mid] - mid - 1
    #
    #         if missing_numbers < k:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    #     return left + k


sol = Solution()
arr = [4, 5, 6, 7]  # [1,2]
k = 2  # 3
k_value = sol.findKthPositive(arr, k)
print(k_value)
