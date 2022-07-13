# first approach with string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        return False


# using integer
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        inputNum = x
        newNum = 0
        while x>0:
            newNum = newNum * 10 + x%10
            x = x//10
        return newNum == inputNum
'''