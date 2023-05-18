"""
# num 5! = 120
factorial(5) = 5 * factorial(4) ^ 24
factorial(4) = 4 * factorial(3) ^ 6
factorial(3) = 3 * factorial(2) ^ 2
factorial(2) = 2 * factorial(1) ^ 1
factorial(1) = 1 * factorial(0) 1
factorial(0) = 1
"""


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("enter"))
print(factorial(num))
