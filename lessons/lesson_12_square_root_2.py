"""
6.00.1X LECTURE 39
GUESS AND CHECK
Remember our “declarative” definition of square root for x
If we could guess possible values for square root (call it g),
then can use definition to check if g*g = x
We just need a good way to generate guesses
One way to use this idea of generating guesses in order to find a cube root of x
is to first try 0**2, then 1**2, then 2**2, and so on
 Can stop when reach k such that k**2 > x Only a finite number of cases to try
"""

x = int(input('Enter an integer: '))
ans = 0
while ans**2 < x:
    ans = ans + 1
if ans**2 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))