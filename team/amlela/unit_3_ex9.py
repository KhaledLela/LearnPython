"""
# https://simplycoding.in/star-pattern-programs-in-python/
Write a python program to print revers hill star pattern:
*      *      *      *      *      *      *      *      *
       *      *      *      *      *      *      *
              *      *      *      *      *
                     *      *      *
                            *
"""
n = int(input("Enter the size:\n"))
for i in range(n):
    for j in range(i):
        print(" ", end="  ")
    for j in range(i, n-1):  # i = 5
        print("*", end="  ")
    for j in range(i,n):
        print("*", end="  ")
    print()