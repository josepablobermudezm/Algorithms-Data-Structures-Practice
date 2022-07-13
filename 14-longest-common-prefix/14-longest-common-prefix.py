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


#Second Approach without extra variables and using the lenght of the min string as main loop

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minString = min(strs,key=len)
        for idy, y in enumerate(minString):
            for other in strs:
                if other[idy] != y:
                    return minString[:idy]
        return minString 

'''

# Third Approach using alphabetic order of min and max lengh

class Solution:
    def longestCommonPrefix(self, m):
        if not m: return ''
		#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
 '''           
                
        