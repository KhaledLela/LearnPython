"""
https://www.py4e.com/html3/09-dictionaries
"""

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] += 1
# print(d)


word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)
#
# counts = {'chuck': 1, 'annie': 42, 'jan': 100}
#
# print(counts.get('kh', 0))
