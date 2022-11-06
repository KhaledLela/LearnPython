"""
Try except statement
"""
try:
    # x = 3 + "hi"
    x = int("3.5")
    print(x)
except (ValueError, TypeError):
    print("value or type error")
except ZeroDivisionError:
    print("zero div error")
except Exception:
    print("other error")









# try:
#     1 / 0
#     print("after error")
# except ZeroDivisionError:
#     print("zero div error")
# except Exception:
#     print("ZeroDivisionError error")
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
