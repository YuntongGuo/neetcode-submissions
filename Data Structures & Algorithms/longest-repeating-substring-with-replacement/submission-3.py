class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = {} 
        if len(s) <= k:
            return len(s)
        l = 0
        r = 0
        window[s[r]] = window.get(s[r],0) + 1
        while r<len(s):
            # print("location",l,r)
            # print(longest)
            window_size = r-l+1
            max_char = 0
            for i in window.values():
                max_char = max(max_char,i)
            if max_char + k >= window_size:
                # print(max_char,window_size)
                longest = max(window_size, longest)
                # print("valid",longest)
                r +=1
                if r<len(s):
                    window[s[r]] = window.get(s[r],0) + 1
            else:
                window[s[l]] = window.get(s[l],0) - 1
                l +=1
        return longest
            