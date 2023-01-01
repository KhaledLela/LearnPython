from unittest import TestCase


class Solution:
    triplets: []

    def search(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2  # make sure to round it down
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def twoSum(self, nums: [int], x: int):
        seen_indexed_map = {}
        for j in range(len(nums)):  # O(n)
            y = nums[j]
            z = (x + y) * -1
            if z in seen_indexed_map and [x, y, z] not in self.triplets:  # O(1)
                self.triplets.append([x, y, z])
            seen_indexed_map[y] = j

    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        self.triplets = []
        for i in range(len(nums)):
            x = nums[i]
            self.twoSum(nums[i+1:], x)
        return self.triplets

    def add_triplet(self, triplet, triplets):
        triplet.sort()
        if triplet not in triplets:
            triplets.append(triplet)


sol = Solution()
actual = sol.threeSum(nums=[-1,0,1,2,-1,-4])
print(actual)


class TestSol(TestCase):
    def test_benchmark(self):
        sol = Solution()
        actual = sol.threeSum(nums=[-2, 0, 1, 1, 2])
        expected = [[-2, 0, 2], [-2, 1, 1]]
        self.assertEqual(actual, expected)
