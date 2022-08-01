from unittest import TestCase


class Solution:
    # O(n2)
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):  # O(n)
            for j in range(i + 1, len(nums)):  # O(n)
                if nums[i] + nums[j] == target:  # O(1)
                    return [i, j]

    # O(n)
    def twoSumEhanced(self, nums: [int], target: int) -> [int]:
        seen_indexed_map = {}
        for i in range(len(nums)):  # O(n)
            val = nums[i]
            com = target - val
            if com in seen_indexed_map:  # O(1)
                return [i, seen_indexed_map[com]]
            seen_indexed_map[val] = i


sol = Solution()
actual = sol.twoSum([2, 7, 11, 15], 9)
print(actual)


class TestSol(TestCase):
    def test_benchmark(self):
        sol = Solution()
        self.assertEqual(sol.twoSumEhanced([2, 7, 11, 15], 9), [1, 0])
