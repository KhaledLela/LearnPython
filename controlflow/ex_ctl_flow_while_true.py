# https://www.py4e.com/html3/05-iterations

# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.

numSum = 0
numCount = 0
while True:  # 10,2,3
    num = input('Enter a number:')
    try:
        num = int(num)
        numSum += num
        numCount += 1
    except ValueError:
        if num == 'done':
            break
        print('Please enter only numbers or done after finish!')


print(numSum, numCount, numSum / numCount)
