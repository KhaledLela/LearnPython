"""
Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
Hints: (ملاحظات)
- def print(self, *args, sep=' ', end='\n', file=None)
- print same line = الطباعة فى نفس السطر
- end = implicit '\n' change to end =""
"""
num = int(input("Enter the size:\n"))
for i in range(1, num):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("")

for i in range(num, 1, -1):  # i = 5
    for j in range(1, i+1):
        print("*", end=" ")
    print("")
