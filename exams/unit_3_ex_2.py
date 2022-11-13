"""
Write a program ask user for
input a list of a comma separated numbers
Then go through each element to calculate max & min

2,3,10,0,-1,-8
"""
s = input('Enter a list of a comma separated nums:\n')
nums = list(map(int, s.split(',')))

max = None
min = None
for el in nums:
    if max is None or max < el:
        max = el
    if min is None or min > el:
        min = el

print('Max is', max)
print('Min is', min)
