# Exercise 1: Write a program which repeatedly reads numbers
# until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers.
# If the user enters anything other than a number,
# detect their mistake using try and except and print an error message
# and skip to the next number.


# total, count, average
# average = total / count
# Invalid div 0/0
value = None
total = 0
count = 0
while value != 'done':
    value = input("Enter number:\n")
    if value != 'done':
        total += int(value)
        count += 1

print("Total= " + str(total))
print("Count= " + str(count))
print("average= " + str(total/count))

