class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reverse_string = s[::-1].rstrip().lstrip()
        
        if ' ' in reverse_string:
            for idx, x in enumerate(reverse_string):
                if(x == ' '):
                    return len(reverse_string[:idx])
        
        return len(reverse_string)

        