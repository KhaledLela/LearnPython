"""
Write a program ask user for
input a list of a comma separated numbers
1 2 3 4 55 66
1,2,3,4,55,66
"""
s = input('Enter a list of a comma separated nums:\n')
str_nums = s.split(',')
print(str_nums)
# nums = []
# for i in range(len(str_nums)):
#     print(i)
#     nums.append(int(str_nums[i]))
# print(nums)

# for n in str_nums:
#     nums.append(int(n))
# print(nums)

# nums = list(map(int,str_nums))
# print(nums)
nums = list(map(float,str_nums))
print(nums)