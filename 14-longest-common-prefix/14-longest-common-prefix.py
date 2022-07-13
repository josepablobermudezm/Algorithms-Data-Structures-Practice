class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        final = ''
        minString = min(strs, key=len)
        print(minString)
        strs.remove(minString)
        print(strs)
        for idy, y in enumerate(strs):
            for idx, x in enumerate(minString):
                print(minString[idx], '==', y[idx])
                if minString[idx] == y[idx]:
                    final = minString[:idx+1]
                elif minString[idx] != y[idx] and len(minString) == 1: 
                    final = ''
                    break
                else:
                    break
            minString = final 
            print(minString)
        return final
            
                
        