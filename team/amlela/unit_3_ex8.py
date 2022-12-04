"""
# https://simplycoding.in/star-pattern-programs-in-python/
Write a python program to print following hill star pattern:
                             *
                      *      *      *
               *      *      *      *      *
        *      *      *      *      *      *      *
"""
n = int(input("Enter the size:\n"))
for i in range(n):
    for j in range(i, n):
        print(" ", end="  ")
    for j in range(i):  # i = 5
        print("*", end="  ")
    for j in range(i+1):
        print("*", end="  ")
    print()
