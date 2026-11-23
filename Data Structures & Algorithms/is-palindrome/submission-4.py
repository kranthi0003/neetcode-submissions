class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = s
        s = "".join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True

