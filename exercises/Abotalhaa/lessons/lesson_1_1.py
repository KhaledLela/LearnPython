num = int(input('Enter number:\n'))
while True:
    if num < 2:
        print('Not a prime number')
        break
    for i in range(2, num):
        if num % i == 0:
            print('Not a prime number')
            break
    else:
        print('prime number ' + '\"' + str(num) + '\"')
        break


