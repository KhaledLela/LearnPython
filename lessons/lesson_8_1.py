# try1_stmt ::=  "try" ":" suite
#                ("except" [expression ["as" identifier]] ":" suite)+
#                ["else" ":" suite]
#                ["finally" ":" suite]
# try2_stmt ::=  "try" ":" suite
#                "finally" ":" suite

# 1. Exception handlers
try:
    print("try block")
except (ValueError, ArithmeticError):
    print("except block")
except TypeError:
    print("type error")
except Exception:
    print("exception")
except:
    print()
else:
    print("else block!")
finally:
    print("finally block!")

# 2. Cleanup code | release resources
try:
    print("try block")
finally:
    print("finally block!")