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

# def isPalindrome(x: int) -> bool:
#     return x >= 0 and x == int(str(x)[::-1])


# Function to check Palindrome
# 121
# 121
# 1234
# 5 * 10
# 50 + 4
# 54321
# / division return float  3/2 = 1.5, 4/2 = 2.0
# // int division 3//2 = 1 & 4/2 = 2
# % remainder division 3 % 2 = 1; 4 % 2 = 0
#  / 10 = 2345
# 0

# 54320
# 11345
#  10 | 12345
#   1 | 10
#     | 1345
#     | 10
#     | 345
#     | 45
#     | 40
#     | 5
# print()

# x = 12345 / 10 = 1234.5, 12345 // 10 = 1234
# x_cut = 12345
# r = 5

def checkPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    # reversed_num = 0
    # x_cut = x
    # while x_cut > 0:  # Exit condition 54321
    #     reversed_num = reversed_num * 10 + x_cut % 10
    #     x_cut //= 10  # x_cut = x_cut // 10 # Base condition
    # return x == reversed_num

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
