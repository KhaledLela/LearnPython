s = "abcdefgh"
# print(s[2])  # c
# print(s[2:4])  # cd range s[i:j] i = inclusive & j=exclusive
# print(s.lower())
# islower()
# capitalize()
# print(s[0].islower())
# if s[0].islower():
#     print(s.capitalize())
# immutable
# del s[0]
# s[0] = "z"

# Data types
# int, float, boolean, NoneType, string

# Data structure

# List mutable
# l1 = [3, 4, 5, 7, 8, 9]
# l2 = [3.2, 4, 5.5, 6]
# l3 = ['a', 3, 4, None, True, False]
# print(l1,l2,l3)
# nums = [2, 3, 4, 5, 6]  # mutable
# print(nums)
# del nums[1]
# print(nums)
#
# points = [[1, 2], [3, 4], [0, 1]]
# print(points[2][0]) # 0
# points[1] = [2,6]
# print(points)

# tuple immutable
# t1 = (3, 4, 5, 6)
# print(t1[0])
# del t1[0]  # 'tuple' object doesn't support item deletion
# t1[0] = 2 # Tuples don't support item assignment
# t2 = ((1, 0), (0, 1), (2, 3))
# print(t2[2][1]) # 3

# dict mutable
d1 = {
    "name": "Khaled",
    "job": "developer",
    "age": 37
}

# print(d1.get('name'))
# print(d1['name'])
# d1["name"] = "Ahmed"
# print(d1)
# del d1["name"]
# print(d1)

# for key in d1:
#     print(key)

# for value in d1.values():
#     print(value)

# for k, v in d1.items():
#     print(k, 'is', v)

for k in d1.keys():
    print(k , 'is', d1[k])
