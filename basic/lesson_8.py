"""
Try statement
"""
try:
    1 / 0
    print("after error")
except ZeroDivisionError:
    print("ZeroDivisionError error")
except (RuntimeError, ArithmeticError):
    print("ZeroDivisionError error")
except Exception:
    print("ZeroDivisionError error")
# try:
#     1/0
#     # raise Exception
#     raise ValueError
#     print("after error")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("ZeroDivisionError error")
# except:
#     print("Other error")
# else:
#     1/0

# try:
#     1 / 0
# finally:
#     print(42)
