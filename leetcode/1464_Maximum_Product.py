from typing import List
from unittest import TestCase


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = self.merge_sort(nums)  # This will sort the list in ascending order
        count = len(nums)
        _1st = nums[count - 1]
        _2nd = nums[count - 2]

        return (_1st - 1) * (_2nd - 1)

    def bubble_sort(self, L):
        swap = False
        while not swap:
            swap = True
            for j in range(1, len(L)):  #
                if L[j - 1] > L[j]:
                    swap = False
                    temp = L[j]
                    L[j] = L[j - 1]
                    L[j - 1] = temp

    def selection_sort(L):
        suffixSt = 0
        while suffixSt != len(L):
            for i in range(suffixSt, len(L)):
                if L[i] < L[suffixSt]:
                    L[suffixSt], L[i] = L[i], L[suffixSt]
            suffixSt += 1

    def merge_sort(self, L):
        print('merge sort: ' + str(L))
        if len(L) < 2:
            return L[:]
        else:
            middle = len(L) // 2
            left = self.merge_sort(L[:middle])
            right = self.merge_sort(L[middle:])
            return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while (i < len(left)):
            result.append(left[i])
            i += 1
        while (j < len(right)):
            result.append(right[j])
            j += 1
        return result


class TestSol(TestCase):
    # def test_fib(self):
    # Ran 1 test in 1.592s
    # self.assertEqual(Solution().fib(38), 63245986)

    def test_fib_efficient(self):
        # Ran 1 test in 0.002s
        self.assertEqual(Solution().fib_efficient(38), 6324598)
