# mutable =
# def f(a, l=[]):
#     l.append(a)
#     return l

# This will print
#
# [1]
# [1, 2]
# [1, 2, 3]


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# This will print
#
# [1]
# [2]
# [3]

print(f(1,[2,3])) # ?? [2,3,1]
print(f(2))
print(f(3))