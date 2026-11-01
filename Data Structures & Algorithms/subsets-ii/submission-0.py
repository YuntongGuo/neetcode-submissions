class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        def dfs(acc,idx):
            if idx > len(nums):
                return 
            results.append(acc.copy())
            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                acc.append(nums[i])
                dfs(acc,i+1)
                acc.pop()
        dfs([],0)
        return results