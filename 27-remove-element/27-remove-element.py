class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for idy, y in enumerate(nums):
            if y != val:
                nums[x] = nums[idy]
                x = x + 1
        return x
    
