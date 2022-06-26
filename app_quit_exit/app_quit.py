# Python program to demonstrate
# quit()
# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit

for i in range(10):

    # If the value of i becomes
    # 5 then the program is forced
    # to quit
    if i == 5:
        # prints the quit message
        print(quit)
        quit()
        # الدالة ممكن تأخذ منك رسالة نصية او كود خروج
        # quit(10)
        # quit('غير مسموح بالسن أقل من ١٥ سنة')
    print(i)
