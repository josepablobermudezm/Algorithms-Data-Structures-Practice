
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idy, y in enumerate(nums):
            for idx, x in enumerate(nums[1:], start = 1):
                if(y + x == target and idy != idx):
                    return [idy] + [idx]
                    
        