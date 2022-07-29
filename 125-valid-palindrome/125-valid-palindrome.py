class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(filter(str.isalnum, s)).lower()
        print(a)
        if a == a[::-1]:
            return True
        
        return False
        