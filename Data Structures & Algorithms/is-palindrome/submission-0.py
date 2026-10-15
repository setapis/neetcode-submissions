class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''

        for i in s:
            if i.isalnum():
                cleaned += i.lower()
        
        right = 0

        if cleaned == cleaned[::-1]:
            return True
        else:
            return False