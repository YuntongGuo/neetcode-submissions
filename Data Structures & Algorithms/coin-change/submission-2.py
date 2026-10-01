class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num = [-1] * (amount+1)
        if amount == 0:
            return 0
        for c in coins:
            if c<=amount:
                num[c] = 1

        for i in range(len(num)):
            if num[i] != -1:
                continue
            min_count = 10001
            for c in coins:
                if i-c >= 0 and num[i-c] != -1:
                    min_count = min(min_count, num[i-c] + 1) 
            if min_count == 10001:
                min_count = -1
            num[i] = min_count
        print(num)
        return num[-1]