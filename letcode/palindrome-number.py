# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.
#
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefor it is not a palindrome.
#
# Constraints:
# * -231 <= x <= 231 - 1
#
# Follow up: Could you solve it without converting the integer to a string?

def isPalindrome(x: int) -> bool:
    if x < 0: return False
    return x >= 0 and x == int(str(x)[::-1])


# Function to check Palindrome
def checkPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return reversed_num == x or x == reversed_num // 10


num = int(input("Enter a number to check if palindrome:\n"))
if checkPalindrome(num):
    print(num, 'is palindrome')
else:
    print(num, 'is not palindrome')
