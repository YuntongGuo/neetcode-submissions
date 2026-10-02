class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoize = [False] * (len(s)+1)
        memoize[0] = True
        for i in range(len(s)+1):
            for w in wordDict:
                if memoize[i]:
                    continue
                if i >= len(w) and s[i-len(w):i] == w:
                    memoize[i] = memoize[i] or memoize[i-len(w)]
        return memoize[-1]        
