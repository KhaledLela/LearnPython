num = 5
for i in range(num - 1):
    for j in range(i, num):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()
for i in range(num):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(i, num - 1):
        print('*', end=' ')
    for j in range(i, num):
        print('*', end=' ')
    print()
