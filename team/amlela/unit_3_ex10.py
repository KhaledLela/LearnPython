"""
# https://www.codesansar.com/python-programming-examples/print-butterfly-pattern.htm
# https://www.educative.io/answers/how-to-generate-a-butterfly-pattern-using-stars-in-python
# Write a program to print butterfly pattern made of stars up to n number of lines given by user.
*                     *
* *                 * *
* * *             * * *
* * * *         * * * *
* * * * *     * * * * *
* * * * * * * * * * * *
* * * * * * * * * * * *
* * * * *     * * * * *
* * * *         * * * *
* * *             * * *
* *                 * *
*                     *
"""
row = int(input("Enter number of rows (even): "))

n = row//2

print("Generated butterfly pattern is:\n")
# Upper part
for i in range(1,n+1):
    for j in range(1, 2*n+1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print("* ", end="")
    print()

# Lower part
for i in range(n,0,-1):
    for j in range(2*n,0,-1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print("* ", end="")
    print()
