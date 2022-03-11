# https://ar.wikipedia.org/wiki/عدد_فيبوناتشي
# https://en.wikipedia.org/wiki/Fibonacci_number

# عمل برنامج لإيجاد عدد فيبوناتشي
# 0,1,1,2,3,5,8,13,21,....,n عدد فيبوناتشي
# fib(n=8) = ?? 

# معلومة 
# fib(1) = 1 & fib(2)= 1
# fib(n) = f(n-2) + fib(n-1)

# Solution = الحل
#fib(n=8) = fib(7) + fib(6)
#fib(n=7) = fib(6) + fib(5)
#fib(n=6) = fib(5) + fib(4)
#fib(n=5) = fib(4) + fib(3)
#fib(n=4) = fib(3) + fib(2)
#fib(n=3) = fib(2) + fib(1) // معلومة

#fib(n=8) =13 + 8 = 21
#fib(n=7) = 8 + 5 = 13
#fib(n=6) = 5 + 3 = 8
#fib(n=5) = 3 + 2 = 5
#fib(n=4) = 2 + 1 = 3
#fib(n=3) = 1 + 1 = 2

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

## call func to print fib of index 8
print(fib(8)) # result 21