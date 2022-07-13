class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for idx, x in enumerate(s):
            if x == 'I':
                num = num + 1
            elif x == 'V' and s[idx - 1] == 'I' and idx != 0:
                num = num + 3
            elif (x == 'V' and s[idx - 1] != 'I') or (x == 'V' and idx == 0):
                num = num + 5
            elif x == 'X' and s[idx - 1] == 'I' and idx != 0:
                num = num + 8
            elif (x == 'X' and s[idx - 1] != 'I') or (x == 'X' and idx == 0):
                num = num + 10
            elif x == 'L' and s[idx - 1] == 'X' and idx != 0:
                num = num + 30
            elif (x == 'L' and s[idx - 1] != 'X') or (x == 'L' and idx == 0):
                num = num + 50
            elif x == 'C' and s[idx - 1] == 'X' and idx != 0:
                num = num + 80
            elif (x == 'C' and s[idx - 1] != 'X') or (x == 'C' and idx == 0):
                num = num + 100
            elif x == 'D' and s[idx - 1] == 'C' and idx != 0:
                num = num + 300
            elif (x == 'D' and s[idx - 1] != 'C') or (x == 'D' and idx == 0):
                num = num + 500
            elif x == 'M' and s[idx - 1] == 'C' and idx != 0:
                num = num + 800
            elif (x == 'M' and s[idx - 1] != 'C') or (x == 'M' and idx == 0):
                num = num + 1000
            print(num, x, s[idx - 1])
        return num
            
        