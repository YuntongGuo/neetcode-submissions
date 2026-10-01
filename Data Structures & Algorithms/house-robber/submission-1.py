class Solution:
    def rob(self, nums: List[int]) -> int:
        memoize = [-1] * (len(nums))

        def recur(i):
            if i < 0:
                return 0
            if memoize[i] != -1:
                return memoize[i]
            max_robbed = max(recur(i-1), recur(i-2) + nums[i])
            # print(max_robbed)
            memoize[i] = max_robbed
            return memoize[i]
        result = recur(len(nums)-1)
        # print(memoize)
        return result
            
