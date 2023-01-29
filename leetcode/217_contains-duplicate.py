"""
https://leetcode.com/problems/contains-duplicate/

217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from unittest import TestCase


class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        """
        1. The first method uses a seen list to store the elements that have been encountered in the input list.
        For each element in the input list, it checks if the element is already in the seen list, and if it is,
        it returns True. Time complexity: O(n), Space complexity: O(n)
        """
        # seen = []
        # for num in nums:
        #     if num in seen: return True
        #     seen.append(num)

        """
        2. The second method uses a for loop to iterate through the input list, 
        and checks if the current element is in the rest of the list.
         Time complexity: O(n^2), Space complexity: O(1)
        """

        for i in range(len(nums)):
            if nums[i] in nums[i + 1:]: return True

        """
        3. The third method uses nested for loops to compare each element to every other element in the input list. 
        Time complexity: O(n^2), Space complexity: O(1)
        """
        # for i in range(len(nums)):
        # for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]: return True

        """
        4. The fourth method converts the input list to a set,
          and then compares the length of the input list to the length of the set.
          If they are not the same, there are duplicates in the input list, 
          and it returns True. Time complexity: O(n), Space complexity: O(n)
        """
        # return len(nums) != len(set(nums))

        """
        5. The fifth method sorts the input list, 
         and then iterates through the list comparing each element to the next element.
         If they are the same, it returns True.
         Time complexity: O(n log n), Space complexity: O(1)
        """
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]: return True
        return False


class TestSol(TestCase):
    def test_valid_parentheses(self):
        nums = [1, 2, 3, 1]
        expected = True

        nums = [1, 2, 3, 4]
        expected = False

        nums = [29797, 29798, 29799, 29800, 29801, 29802, 29803, 29804, 29805, 29806, 29807, 29808, 29809, 29810, 29811,
                29812, 29813, 29814, 29815, 29816, 29817, 29818, 29819, 29820, 29821, 29822, 29823, 29824, 29825, 29826,
                29827, 29828, 29829, 29830, 29831, 29832, 29833, 29834, 29835, 29836, 29837, 29838, 29839, 29840, 29841,
                29842, 29843, 29844, 29845, 29846, 29847, 29848, 29849, 29850, 29851, 29852, 29853, 29854, 29855, 29856,
                29857, 29858, 29859, 29860, 29861, 29862, 29863, 29864, 29865, 29866, 29867, 29868, 29869, 29870, 29871,
                29872, 29873, 29874, 29875, 29876, 29877, 29878, 29879, 29880, 29881, 29882, 29883, 29884, 29885, 29886,
                29887, 29888, 29889, 29890, 29891, 29892, 29893, 29894, 29895, 29896, 29897, 29898, 29899, 29900, 29901,
                29902, 29903, 29904, 29905, 29906, 29907, 29908, 29909, 29910, 29911, 29912, 29913, 29914, 29915, 29916,
                29917, 29918, 29919, 29920, 29921, 29922, 29923, 29924, 29925, 29926, 29927, 29928, 29929, 29930, 29931,
                29932, 29933, 29934, 29935, 29936, 29937, 29938, 29939, 29940, 29941, 29942, 29943, 29944, 29945, 29946,
                29947, 29948, 29949, 29950, 29951, 29952, 29953, 29954, 29955, 29956, 29957, 29958, 29959, 29960, 29961,
                29962, 29963, 29964, 29965, 29966, 29967, 29968, 29969, 29970, 29971, 29972, 29973, 29974, 29975, 29976,
                29977, 29978, 29979, 29980, 29981, 29982, 29983, 29984, 29985, 29986, 29987, 29988, 29989, 29990, 29991,
                29992, 29993, 29994, 29995, 29996, 29997, 29998, 29999]
        expected = False
        self.assertEqual(Solution().containsDuplicate(nums), expected)
