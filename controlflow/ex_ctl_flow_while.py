# https://www.py4e.com/html3/05-iterations

# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

# >>> while True:
# ...     try:
# ...         x = int(input("Please enter a number: "))
# ...         break
# ...     except ValueError:
# ...         print("Oops!  That was no valid number.  Try again...")
# ...
# if isinstance(num, int):

num = None
numSum = 0
numCount = 0
while num != 'done':  # 10,2,3
    num = input('Enter a number:')
    try:
        num = int(num)
        numSum += num
        numCount += 1
    except ValueError:
        print('Please enter only numbers or done after finish!')

print(numSum, numCount, numSum / numCount)
