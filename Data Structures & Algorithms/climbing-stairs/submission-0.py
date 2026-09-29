class Solution:
    def climbStairs(self, n: int) -> int:
        memoize = [0] * (n+1)
        memoize[0] = 1
        for i in range(len(memoize)):
            if i > 0:
                memoize[i] += memoize[i-1]
            if i > 1:
                memoize[i] += memoize[i-2]
        return memoize[-1]