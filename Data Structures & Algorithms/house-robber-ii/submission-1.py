class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        def max_price(houses):
            memoize = [-1] * len(houses)
            def dfs(i):
                if i >= len(houses):
                    return 0
                if memoize[i] != -1:
                    return memoize[i]
                memoize[i] = max(dfs(i+1), dfs(i+2)+houses[i])
                return memoize[i]
            return dfs(0)

        result = max(max_price(nums[1:]), max_price(nums[:-1]))
        
        return result