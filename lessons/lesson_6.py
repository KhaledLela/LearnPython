"""
Exercise 1: Write a program which repeatedly reads numbers
 until the user enters “done”. Once “done” is entered,
 print out the total, count, and average of the numbers.
 If the user enters anything other than a number,
 detect their mistake using try and except and print an error message
 and skip to the next number.
"""

# total, count, average
# average = total / count
# Invalid div 0/0

"""
Value user input
When user enter done stop
"""
value = None
total = 0
count = 0
while value != 'done':
    value = input("Enter number:\n")
    if value != 'done':
        try:
            total += int(value)
            count += 1
        except ValueError:
            print("On Error:: Should be number or done")
        else:
            print("Else:: other error!")
        finally:
            print("Finally:: Release")
print("Total= " + str(total))
print("Count= " + str(count))
try:
    print("average= " + str(total/count))
except ZeroDivisionError:
    print("You should at least enter one value")

