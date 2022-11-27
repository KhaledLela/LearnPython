num = int(input('Enter number:\n'))
if num < 2:
    print('Not a prime number ' + '\"' + str(num) + '\"')
else:
    for i in range(2, num):
        if num % i == 0:
            print('Not a prime number ' + '\"' + str(num) + '\"')
            break
    else:
        print('prime number ' + '\"' + str(num) + '\"')


