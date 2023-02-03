# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#  a, b = b, a + b
#     print()
# def keyword to define the function.
# variables inside func called local variables
# store the value in the local symbol table

# Scope
# index

def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    # a = 0
    # b = 1
    a, b = 0, 1
    while a < n:
        print(a, end=' ')



# >>> # Now call the function we just defined:
fib(100)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987                 GDY7YHGY 5UJUGYU8UYGHEDF8GGTGT