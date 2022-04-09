# List numbers - max & min
import json
import ast

# numStr = input("Enter List of numbers: \n")
# numbers = json.loads(numStr)
# numbers = ast.literal_eval(numStr)

numbers = [10, 2, 3, 1, 30, 5]
maxNum = None
minNum = None

for n in numbers:
    if maxNum is None or maxNum < n:
        maxNum = n
    if minNum is None or minNum > n:
        minNum = n
print(maxNum)
print(minNum)
