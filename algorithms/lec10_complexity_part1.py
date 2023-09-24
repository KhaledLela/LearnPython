# # -*- coding: utf-8 -*-
# """
# Created on Sun Oct  9 11:27:54 2016
#
# @author: ericgrimson
# """
#
def linear_search(L, e):   # O(n)
    found = False   # O(1)
    for i in range(len(L)): # (n)
        if e == L[i]:
            found = True
    return found  # O(1)
#
# testList = [1, 3, 4, 5, 9, 18, 27]
#
def search(L, e):     # O(n)
    for i in range(L):  # O(n)
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False  # O(1)
#
#
# def isSubset(L1, L2):
#     for e1 in L1:
#         matched = False
#         for e2 in L2:
#             if e1 == e2:
#                 matched = True
#                 break
#         if not matched:
#             return False
#     return True
#
#
# testSet = [1, 2, 3, 4, 5]
# testSet1 = [1, 5, 3]
# testSet2 = [1, 6]
#
# def intersect(L1, L2):
#     tmp = []
#     for e1 in L1:
#         for e2 in L2:
#             if e1 == e2:
#                 tmp.append(e1)
#     res = []
#     for e in tmp:
#         if not(e in res):
#             res.append(e)
#     return res

def fact_int(n):
    result = 1                  # O(1)
    for i in range(1, n + 1):   # O(2n)
        result *= i             # O(2n)
    return result               # O(1)


# 1 + 4n + 1
# O(n)


x = fact_int(3)
print(x)