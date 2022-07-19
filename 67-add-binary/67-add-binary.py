class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a, b = (a, b) if len(a) > len(b) else (b, a)
        carry = 0
        array = []
        
        for x in reversed(range(len(b))):
            print(a[x+(len(a) - len(b))], b[x])
            if a[x+(len(a) - len(b))] == '1' and b[x] == '0' or b[x] == '1' and a[x+(len(a) - len(b))] == '0':
                if carry == 0:
                    array.insert(0, 1)
                    carry = 0
                else:
                    array.insert(0, 0)
                    carry = 1
            elif a[x+(len(a) - len(b))] == '1' and b[x] == '1':
                if carry == 0:
                    carry = 1
                    array.insert(0, 0)
                else:
                    carry = 1
                    array.insert(0, 1)
            else:
                if carry == 1:
                    array.insert(0, 1)
                    carry = 0
                else:
                    array.insert(0, 0)
        
        for x in reversed(range(len(a) - len(b))):
            if (carry == 0 and a[x] == '1') or (carry == 1 and a[x] == '0'):
                array.insert(0, 1)
                carry = 0
            elif a[x] == '1' and carry == 1:
                carry = 1
                array.insert(0, 0)
            else:
                array.insert(0, 0)
        
        if carry == 1:
            array.insert(0, 1)
            
        return ''.join([str(a) for a in array])

        