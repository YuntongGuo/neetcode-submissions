class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_max = -10001
        acc_max = -10001
        for n in nums:
            acc_max = max(n,acc_max+n)
            final_max = max(acc_max,final_max)
        return final_max