'''

#First approach
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        for idx, x in enumerate(nums):
            if target == x:
                return idx
            elif nums[idx+1] > target:
                return idx+1
                
'''     

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid=(l+r) // 2
            print('mid', mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l