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
                
        