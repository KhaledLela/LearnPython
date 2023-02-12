"""
# num 5! = 120
f(5) = 5 * f(4) = 120
f(4) = 4 * f(3) = 24
f(3) = 3 * f(2) = 6
f(2) = 2 * f(1) = 2
f(1) = 1 * f(0) = 1
f(0) = 1

"""


def f(n):
    if n < 1:
        return 1
    else:
        return n * f(n - 1)


num = int(input("enter"))
print(f(num))
