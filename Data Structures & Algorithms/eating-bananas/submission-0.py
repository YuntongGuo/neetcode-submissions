class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish_with_k(k):
            time = 0
            for i in piles:
                time += i//k
                if i% k != 0:
                    time +=1
            return time <= h
        # find the min k
        l = 1 
        r = max(piles)+1
        while l < r:
            m = (l+r)//2
            if finish_with_k(m):
                r = m
            else:
                l = m+1
        return l