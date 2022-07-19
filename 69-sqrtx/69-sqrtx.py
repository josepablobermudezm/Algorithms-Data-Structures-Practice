'''
#First Approach
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

'''
class Solution:            
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1