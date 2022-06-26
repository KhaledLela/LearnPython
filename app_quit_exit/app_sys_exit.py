# Python program to demonstrate
# sys.exit()
# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit


import sys

age = 17

if age < 18:

    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
