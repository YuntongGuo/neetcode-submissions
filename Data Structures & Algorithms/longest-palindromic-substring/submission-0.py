class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = 0
        left,right = 0,0
        for c in range(len(s)):
            if c < len(s)-1 and s[c] == s[c+1]:
                length = 2
                l = c-1
                r = c+2
                while 0 <= l < r < len(s) and s[l] == s[r]:
                    length +=2
                    l-=1
                    r +=1
                if length > longest_pal:
                    longest_pal = length
                    left = l+1
                    right = r-1

            length = 1
            l = c-1
            r = c+1
            while 0 <= l < r < len(s) and s[l] == s[r]:
                length +=2
                l -= 1
                r += 1
            if length > longest_pal:
                longest_pal = length
                left = l+1
                right = r-1
        return s[left: right+1]