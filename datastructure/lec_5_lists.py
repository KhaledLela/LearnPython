"""
https://www.py4e.com/html3/08-lists
"""


# Parsing lines
# file = open('/Users/khaledlela/Desktop/mbox.txt')
#
# for line in file:
#     line = line.rstrip()
#     if not line.startswith('From '): continue
#     words = line.split()
#     print(words)

# Objects and values
# a = 'banana'
# b = 'banana'
#
# print(a is b)
#
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a is b)

# Aliasing

# a = 10
# b = a
# print(a is b)
# a += 10
# print(a, b)

# a = [1, 2, 3]
# b = a
# print(b is a)
# print(id(a))
# print(id(b))
# a[1] = 5
#
# print(a, b)

# List arguments
# The function gets a reference to the list.
# The parameter `t` and the variable `a` are aliases for the same object.

# def delete_head(t):
#     t = [0, 2, 4]
#     print(t)

def delete_head(t):
    t = t[1:]
    print(t)


a = [1, 2, 3]
delete_head(a)
print(a)
