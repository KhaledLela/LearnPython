s = input('enter your numbers and separate it by ,:\n')
str_nums = s.split(',')
print(str_nums)
num = []
for n in str_nums:
    num.append(int(n))
print(num)
nums = list(map(int, str_nums))
x = num[0]
# for x in str_nums:
#     print(max(nums))
#     break
# for x in str_nums:
#     print(min(nums))
#     break
# print(max(nums))
# print(min(nums))
for i in range(0, len(num)):
    if num[i] > x:
        x = num[i]
print("the largest number in your list is " + str(x))
for i in range(0, len(num)):
    if num[i] < x:
        x = num[i]
print("the smallest number in your list is " + str(x))
