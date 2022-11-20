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
n=int(input("enter a number:\n "))
if n > 1:
    for i in range(2, n):
        if(n % i) == 0:
            print(n, " is a prime number")
        else:
            print(n, "is not a prime number")
        break
else:
    print(n, 'is not a prime number')
