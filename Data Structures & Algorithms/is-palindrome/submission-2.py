class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_c = ''.join([c.lower() for c in s if c.isalnum()])
        return new_c == new_c[::-1]