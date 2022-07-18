'''

#First Approach

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reverse_string = s[::-1].rstrip().lstrip()
        
        if ' ' in reverse_string:
            for idx, x in enumerate(reverse_string):
                if(x == ' '):
                    return len(reverse_string[:idx])
        
        return len(reverse_string)
        
'''

class Solution:
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while end > 0 and s[end] == " ": 
            end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ": 
            beg -= 1
        return end - beg

        