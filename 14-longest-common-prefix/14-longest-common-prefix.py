'''
#First Approach

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        final = ''
        minString = min(strs, key=len)
        strs.remove(minString)
        for idy, y in enumerate(strs):
            for idx, x in enumerate(minString):
                if minString[idx] == y[idx]:
                    final = minString[:idx+1]
                elif minString[idx] != y[idx] and len(minString) == 1: 
                    final = ''
                    break
                else:
                    break
            minString = final 
        return final
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minString = min(strs,key=len)
        for idy, y in enumerate(minString):
            for other in strs:
                print(other[idy], '=', y)
                if other[idy] != y:
                    return minString[:idy]
        return minString 
            
                
        