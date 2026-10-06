class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(x,n)
        if n == 0:
            return 1

        invert = False
        # half_n = n//2
        if n < 0:
            n = -n
            x = 1/x
        
        if n%2 == 0:
            result = self.myPow(x**2,n//2)
        else:
            result = x * self.myPow(x**2, n//2)

        return result