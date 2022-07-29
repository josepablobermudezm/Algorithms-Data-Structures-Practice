#First Approach

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(filter(str.isalnum, s)).lower()
        print(a)
        if a == a[::-1]:
            return True
        return False
'''

        
# Most Optimal

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        anchor = len(s) - 1

        for i in range(len(s)):
            if s[i].isalnum():
                for j in range(anchor, -1, -1):
                    if i == j:
                        return True
                    if s[j].isalnum():
                        if s[i] == s[j]:
                            anchor = j - 1
                            break
                        else:
                            return False
        
        return True # handle ' '