# https://docs.python.org/3.8/tutorial/controlflow.html#if-statements

x = int(input("Please enter an integer: "))
# Please enter an integer: 42
# and , or , not => boolean
if 0 > x > -5: # True, False
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
