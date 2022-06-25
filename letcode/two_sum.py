# O(n2)
def twoSum(nums: [int], target: int) -> [int]:
    for i in range(len(nums)):  # O(n)
        for j in range(i + 1, len(nums)):  # O(n)
            if nums[i] + nums[j] == target:  # O(1)
                return [i, j]


# O(n)
def twoSumEhanced(nums: [int], target: int) -> [int]:
    seen_indexed_map = {}
    for i in range(len(nums)):  # O(n)
        val = nums[i]
        com = target - val
        if com in seen_indexed_map:  # O(1)
            return [i, seen_indexed_map[com]]
        seen_indexed_map[val] = i


print(twoSumEhanced([2, 7, 11, 15], 9))
