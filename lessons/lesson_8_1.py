# try1_stmt ::=  "try" ":" suite
#                ("except" [expression ["as" identifier]] ":" suite)+
#                ["else" ":" suite]
#                ["finally" ":" suite]
# try2_stmt ::=  "try" ":" suite
#                "finally" ":" suite

# 1. Exception handlers
try:
    exit(1)
    print("No error!")
except ZeroDivisionError:
    print("can't div by zero")
except ArithmeticError:
    print("arithemtic error!")
except Exception:
    print("Exception error!")
# except BaseException:
#     print("Base error!")
# except:
#     print("Base error!")
else:
    print("else block!")
finally:
    print("finally block!")

# 2. Cleanup code | release resources
# try:
#     print("try finally!")
# finally:
#     print("finally block!")
