'''
# First Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idy, y in enumerate(nums):
            for idx, x in enumerate(nums):
                if(y + x == target and idy != idx):
                    return [idy] + [idx]
'''  

class Solution:
    def twoSum(self, nums, target):
        dictionary = {}
        for idx, num in enumerate(nums):
            b = target - num
            if b in dictionary:
                return [dictionary[b], idx]
            else:
                dictionary[num] = idx
                
#The key to the problem is that there is ALWAYS only 1 pair of numbers that satisfy the condition of adding together to be the target value.
#We can assume that for all the numbers in the list (x1, x2, ... xn) that there exists a pair such that a + b = target
#To solve this with a single pass of the list we can change the equation above to b = target - a and since we know the target as long as we maintain a record of all previous values in the list we can compare the current value (a) to it's ONLY pair, if it exists, in record of all previous values (b)

#To keep a record of the previous values and their indices I have used a dictionary. Commonly known as a map in other languages. This allows me to record each previous number in the dictionary alongside the indice as a key value pair (target-number, indice).