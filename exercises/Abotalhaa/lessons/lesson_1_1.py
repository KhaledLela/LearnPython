num = int(input('Enter number:\n'))
for i in range(2, num):
    if num % i == 0:
        print(' Not a number prime')
        break
else:
    print('prime number  ' + '\"' + str(num) + '\"')

