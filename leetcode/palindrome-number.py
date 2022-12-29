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
# 121
# 010 != 0
# -010
# 0
# 1
# x_cut = 12345
# r = 5

# 1221
# 0
def checkPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    # 1221
    # 12
    # 1   => %
    # 122 => //

    # 1 + 2 = 3
    # 1 * 10 = 10 + 2 = 12
    reversed_num = 0
    # temp = x
    # while temp > 0:  # Exit condition 1221
        # 1
        # 10 + 2 = 12
        # r = 12
        # 12 * 10 = 120 + 2 = 122
        # r = 122
        # 122 * 10 = 1220 + 1 = 1221
        # 1221
        # 1221 % 10 = 1
        # r = 0 + 1 = 1

        # 122 % 10 = 2
        # r = 1 + 2 = 3
        # r = 1, c = 2, o = 12
        # r * 10 = 10  + 2 = 12

        # r = 12
        # temp = 12
        # c = 12 % 10 = 2
        # r + 2 = 14
        # r * 10 = 120 + 2 = 122
        # r * 10 = 1220 + 1 = 1221
    #     reversed_num = reversed_num * 10 + temp % 10
    #     temp //= 10  # x_cut = x_cut // 10 # Base condition
    # return x == reversed_num


    # x = 1221
    # t = 12
    # r = 12

    # x = 2002

    # t = 20
    # r = 20

    # x = 2010
    # False

    # x = 1553
    # t = 15
    # r = 35

    # x = 121

    # x = 1
    # r = 1
    # False
    # x = 12
    # r = 122
    # r //= 10 = 12

    # 99
    # 99
    # 100

    # 12221
    r = 0
    while x > r:
        r = r * 10 + x % 10
        x //= 10
    return r == x or x == r // 10


num = int(input("Enter a number to check if palindrome:\n"))
if checkPalindrome(num):
    print(num, 'is palindrome')
else:
    print(num, 'is not palindrome')
