class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memoize = [[-1] * len(coins) for _ in range(amount+1)]
        memoize[0][0] = 1
        def recur(a,c):
            # print(a,c)
            if memoize[a][c] != -1:
                return memoize[a][c]
            else:
                memoize[a][c] += 1
                if a-coins[c] >= 0:
                    memoize[a][c] += recur(a-coins[c],c)
                if c > 0:
                    memoize[a][c] += recur(a,c-1)
            return memoize[a][c]
        recur(amount,len(coins)-1)
        return memoize[amount][len(coins)-1]