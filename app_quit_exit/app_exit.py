# Python program to demonstrate
# exit()
# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit

# quit(code=None)
# exit(code=None)
# Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”,
# and when called, raise SystemExit with the specified exit code.

for i in range(10):

    # If the value of i becomes
    # 5 then the program is forced
    # to exit
    if i == 5:
        # prints the exit message
        print(exit)
        exit()
        # الدالة ممكن تأخذ منك رسالة نصية او كود خروج
        # exit(10)
    print(i)
