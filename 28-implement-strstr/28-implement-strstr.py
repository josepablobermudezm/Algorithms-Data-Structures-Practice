'''class Solution:
#first approach
    def strStr(self, haystack: str, needle: str) -> int:
        if (not needle or not haystack):
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        i = 0
        for idx, x in enumerate(haystack):
            if len(haystack[idx:]) >= len(needle):
                if x == needle[i] and len(needle) == 1:
                    return idx
                elif x == needle[i] and len(needle) != 1:
                    i += 1
                    for idy, y in enumerate(needle[1:], start = 1):
                        if haystack[idx+idy] == needle[i]:
                            i += 1
                            if i == len(needle):
                                return idx
                    i = 0
            else:
                return -1
        return -1
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1