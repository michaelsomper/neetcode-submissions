class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())

        if s == s[::-1]:
            return True
        
        return False