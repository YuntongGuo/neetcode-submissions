class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def go(n):
            return nums[n]
        s = 0
        f = 0
        while True:
            s = go(s)
            f = go(go(f))
            if s == f:
                break
        s2 = 0
        while s != s2:
            s = go(s)
            s2 = go(s2)
        return s2