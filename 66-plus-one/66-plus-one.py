'''

#First Approach
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] < 9:
                digits[idx] += 1
                for y in range(idx+1, len(digits)):
                    digits[y] = 0
                return digits
        
        for i in range(len(digits)):
            digits[i] = 0
        digits.insert(0, 1)
        return digits
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(x) for x in str(num+1)]

        