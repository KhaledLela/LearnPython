"""
Write a program ask user for
input a list of a comma separated numbers
1 2 3 4 55 66
1,2,3,4,55,66
"""
s = input('Enter a list of a comma separated nums:\n')
str_nums = s.split(',')
print(str_nums)
# num = []
# for n in str_nums:
#     num.append(int(n))
# print(num)
nums = list(map(int,str_nums))
print(nums)
nums = list(map(float,str_nums))
print(nums)