s = input('enter a list:\n')
str_nums = s.split(',')
print(str_nums)
num = []
for n in str_nums:
    num.append(int(n))
print(num)
nums = list(map(int,str_nums))