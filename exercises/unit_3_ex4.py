# """
# Write a program ask user for input two values
# v1 & v2 and print larger value
# """
v1 = int(input("enter a number:\n"))
v2 = int(input("enter a number:\n"))
if v1 > v2:
    print(v1, "is the large value")
elif v1 < v2:
    print(v2, "is the larger value")
else:
    print("the values are equals")