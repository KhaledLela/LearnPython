# Python program to explain os._exit() method

# importing os module
import os

age = 17

if age < 18:

    # exits the program
    os._exit(os.EX_OK)
else:
    print("Age is not less than 18")
