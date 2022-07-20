class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while nums2:
            nums1[m] = nums2.pop() 
            n = n - 1
            m = m + 1
            
        nums1 = nums1.sort()
            
        