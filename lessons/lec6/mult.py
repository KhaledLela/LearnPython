"""
mult(12,3) = 12 + mult(12,2) = 12 + 24 = 36
mult(12,2) = 12 + mult(12,1) = 12 + 12 = 24
mult(12,1) = 12
"""


def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b - 1)


print(mult(12, 3))
