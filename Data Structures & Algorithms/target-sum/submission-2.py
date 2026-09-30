class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        element_sum = sum(nums)
        memoize = [[-1] * len(nums) for _ in range(2*element_sum+1)]
        if abs(target) > element_sum:
            return 0
        
        def recur(total,num):
            if num < 0:
                return 1 if total == 0 else 0
            if abs(total) > element_sum:
                return 0
            row = total + element_sum
            if memoize[row][num] != -1:
                return memoize[row][num]
            else:
                memoize[row][num] = recur(total-nums[num],num-1) + recur(total+nums[num],num-1)
            return memoize[row][num]
        return recur(target,len(nums)-1)