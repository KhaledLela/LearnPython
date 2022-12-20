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
num = int(input("Enter the size:\n"))  # 12
for i in range(num // 2):
    for j in range(i + 1):  # 6
        print("*", end=" ")
    for s in range((i + 1) * 2, num):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print("")

for i in range(num // 2):
    for j in range(i, num // 2):  # 6
        print("*", end=" ")
    for s in range(i * 2):
        print(" ", end=" ")
    for j in range(i, num // 2):
        print("*", end=" ")
    print("")
