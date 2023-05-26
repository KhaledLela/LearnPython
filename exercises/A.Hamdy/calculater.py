num1 = float(input("enter number:\n"))
operator = input("enter your operator:\n")
num2 = float(input("enter number:\n"))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "^":
    print(num1 ** num2)
elif operator == "%":
    print(num1 % num2)
elif operator == "//":
    print(num1 // num2)
else:
    print("error")
