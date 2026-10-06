class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def step(num):
            acc= 0
            while num!=0:
                d = num%10
                acc+=d**2
                num = num // 10
            return acc
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = step(n)
        return False
