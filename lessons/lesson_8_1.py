# try1_stmt ::=  "try" ":" suite
#                ("except" [expression ["as" identifier]] ":" suite)+
#                ["else" ":" suite]
#                ["finally" ":" suite]
# try2_stmt ::=  "try" ":" suite
#                "finally" ":" suite

# 1. Exception handlers
# try:
#     print("try block")
# except (ValueError, ArithmeticError):
#     print("except block")
# except TypeError:
#     print("type error")
# except Exception:
#     print("exception")
# except:
#     print()
# else:
#     print("else block!")
# finally:
#     print("finally block!")

# 2. Cleanup code | release resources
try:
    exit(0)
except ZeroDivisionError:
    print("You can not divided by zero")
except ArithmeticError as x:
    print("arithmetic error!", x)
except Exception:
    print("exception!")
except BaseException as x:
    print("other error!",x)
finally:
    print("finally block!")
