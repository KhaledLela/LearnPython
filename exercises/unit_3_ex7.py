"""
Write a python program to print the factorial of a given number
https://en.wikipedia.org/wiki/Factorial
https://ar.wikipedia.org/wiki/عاملي
"""
num = int(input("Enter the number:\n"))
factorial = 1
for n in range(2, num + 1):
    factorial *= n
print("Factorial of", num, "is:", factorial)
