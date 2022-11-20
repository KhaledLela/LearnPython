# https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# mutable =
# def f(a, l=[]):
#     l.append(a)
#     return l

# This will print
#
# [1]
# [1, 2]
# [1, 2, 3]


def f(a, m = None):
    if m is None:
        m = []
    m.append(a)
    return m


# This will print
#
# [1]
# [2]
# [3]

print(f(1,[2,3])) # ?? [2,3,1]
print(f(2))
print(f(3))