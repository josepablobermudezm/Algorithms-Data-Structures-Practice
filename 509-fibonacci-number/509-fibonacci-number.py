class Solution:
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            print(a, b)
            a, b = b, a + b
            print(a, b)
        return a
        
        