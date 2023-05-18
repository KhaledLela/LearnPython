# https://docs.python.org/3.8/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
# break and continue Statements, and else Clauses on Loops
def check_range():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

# عمل دالة حتى يمكن استدعائها
def check_pass():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)

# call function - استدعاء الدالة
check_range()
# check_pass()
