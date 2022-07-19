class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        r = 1
        c = 1
        while r <= x:
            r = c * c
            c += 1
        return c-1 if c * c <= x else c-2
            
        