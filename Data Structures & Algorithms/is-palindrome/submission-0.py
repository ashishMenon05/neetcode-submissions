class Solution:
    def isPalindrome(self, s: str) -> bool:
        v="".join(c for c in s if c.isalnum())
        x=v.lower()
        if x==x[::-1]:
            return True
        else:
            return False