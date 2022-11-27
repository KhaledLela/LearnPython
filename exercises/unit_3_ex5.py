"""
https://en.wikipedia.org/wiki/Prime_number
https://ar.wikipedia.org/wiki/%D8%B9%D8%AF%D8%AF_%D8%A3%D9%88%D9%84%D9%8A
Write a program ask user for input
a number and print if this number is a prime number or not.
ex. 5
5 is a prime number.
ex. 9
9 is not a prime number.
"""
num = int(input('enter the number:\n'))
if num < 2:
    print(num, 'is not a prime number')
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, 'is not a prime number!')
            break
    else:
        print(num, 'is a prime number!')
