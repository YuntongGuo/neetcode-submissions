class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        max_len = 0
        for n in num:
            if n-1 in num:
                continue
            c_len = 1
            r = n+1
            while r in num:
                c_len+=1
                r+=1
            max_len = max(max_len,c_len)
        return max_len
