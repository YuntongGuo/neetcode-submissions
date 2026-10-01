class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memoize = [-1] * (len(cost)+1)
        memoize[0] = 0
        memoize[1] = 0
        def recur(i):
            if memoize[i] != -1:
                return memoize[i]
            
            last_cost = recur(i-1) + cost[i-1]
            last_last_cost = recur(i-2) + cost[i-2]
            
            memoize[i] = min(last_cost, last_last_cost)
            return memoize[i]
        
        return recur(len(cost))