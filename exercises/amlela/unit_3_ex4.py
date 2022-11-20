"""
Write a program ask user for input two numbers
print larger value
"""
try:
    n1 = int(input("Enter 1st number:\n"))
    n2 = int(input("Enter 2nd number:\n"))
    if n1 > n2:
        print("Larger number is :", n1)
    elif n1 < n2:
        print("Larger number is :", n2)
    else:
        print("Two numbers are equals!")
except ValueError:
    print("Enter a number")