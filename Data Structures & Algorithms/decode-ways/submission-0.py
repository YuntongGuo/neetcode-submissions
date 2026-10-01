class Solution:
    def numDecodings(self, s: str) -> int:
        memoize = [-1] * (len(s)+1)
        memoize[0] = 1
        memoize[1] = 1
        if s[0] == '0':
            return 0
        for i in range(2,len(memoize)):
            ways = 0
            if s[i-1] != '0':
                ways += memoize[i-1]
            if int(s[i-2:i]) <= 26 and s[i-2] != '0':
                ways += memoize[i-2]
            memoize[i] = ways
        return memoize[-1]