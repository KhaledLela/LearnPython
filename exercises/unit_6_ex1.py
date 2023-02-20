#####################################
# EXAMPLE:  fibonacci using recursion
#####################################

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}
print(fib(10))
