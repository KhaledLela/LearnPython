from math import ceil, floor, factorial, fmod

x = 2.50
y = 2.45
z = 2.75

# print(round(x))  # 2
# print(round(y))  # 2
# print(round(z))  # 2

# print(ceil(x))  # 3
# print(ceil(y))  # 3
# print(ceil(z))  # 3

# print(floor(x))  # 2
# print(floor(y))  # 2
# print(floor(z))  # 2

x = 4
# factorial() only accepts integral values تقبل اعداد صحيحة فقط ولا تقبل كسور
# print(factorial(x)) # 24

x = 7
y = 3
print(x / y)  # 2.3333333333333335
print(round(x / y))  # 2

print(pow(3,3))  # 2


# المتبقى من القسمة
print(x % y)  # 1
print(fmod(x,y))  # 1.0 = x % y

print(sum([x,y,z])) # sum = 7.70
