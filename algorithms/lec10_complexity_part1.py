# # -*- coding: utf-8 -*-
# """
# Created on Sun Oct  9 11:27:54 2016
#
# @author: ericgrimson
# """
#
def linear_search(L, e):  # O(n)
    found = False  # O(1)
    for i in range(len(L)):  # (n)
        if e == L[i]:
            found = True
    return found  # O(1)


#
# testList = [1, 3, 4, 5, 9, 18, 27]
#
def search(L, e):  # O(n)
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

# def fact_int(n):
#     result = 1                  # O(1)
#     for i in range(1, n + 1):   # O(2n)
#         result *= i             # O(2n)
#     return result               # O(1)


# 1 + 4n + 1
# O(n)

#
# x = fact_int(3)
# print(x)


def intToStr(i):
    digits = '9876543210'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10  # 7/10 = 0.7 && 7//10 = 0 && 57%10=7   7/10 O(log n)
    return result


# 1000
# n=1 =>   1000%10 = 0 && 1000//10 = 100
# n=2 =>   100%10  = 0 && 100//10  = 10
# n=3 =>   10%10   = 0 && 10//10   = 1
# n=4 =>   1%10    = 1 && 1//10    = 0


# result = 8999

# print(intToStr(1000))


# log10 10^3 = ?? 3
# log10 10^4 = ?? 4


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None


my_list = [1, 3, 5, 7, 9]
# low and high keep track of which part of the list you’ll search in.
# While you haven’t narrowed it down to one element ...
# ... check the middle element. Found the item.
# The guess was too high. The guess was too low. The item doesn’t exist. Let’s test it!

# print(binary_search(my_list, 3))  # => 1 print binary_search(my_list, -1) # =



