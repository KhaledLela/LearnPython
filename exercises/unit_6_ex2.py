#####################################
# EXAMPLE:  palindrome using recursion
# Base case
# recursive condition.
#####################################
def isPalindrome(s):
    """assumes x an int >= 0
    """
    # Base case
    if len(s) <= 1:
        return True
    else:
        # recursive condition.
        return s[0] == s[-1] and isPalindrome(s[1:-1])
