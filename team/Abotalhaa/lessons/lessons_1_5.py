num = 5
# k = 0
for i in range(num):
    for j in range(i + 1):
        print('*', end=' ')
    # k += 1
    print()
# m = k
for i in range(num, ):
    for j in range(i, num):
        print('*', end=' ')
    # m += 1
    print()
j = 0
for i in range(num):
    for j in range(i, num):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    # j += 1
    print()
# g = j
for i in range(num):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(i, num):
        print('*', end=' ')
    # g += 1
    print()
