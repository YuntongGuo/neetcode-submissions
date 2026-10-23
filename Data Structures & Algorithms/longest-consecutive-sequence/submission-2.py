class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        long_len = 0
        for n in nums:
            if n-1 in num:
                continue
            else:
                c_len = 1
                while n + c_len in num:
                    c_len += 1
                long_len = max(c_len,long_len)

        return long_len

                     