"""
Write a program ask user for
input a list of a comma separated numbers
Then go throw each element to calculate max & min
"""
s = input('Enter a list of a comma separated nums:\n')
str_nums = s.split(',')
print(str_nums)
num=[]

x = [0]

for n in str_nums:
    if  is None or maxnums < n:
        maxnums= n
    if minnums is None or minnums > n:
        minnums = n
print(minnums)
print(maxnums)