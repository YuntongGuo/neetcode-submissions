class Solution:
    def partition(self, s: str) -> List[List[str]]:
        acc = []
        def isPalindrome(p):
            return p == p[::-1]
        def recur(cur,palins,i):
            if i == len(s):
                if len(palins) ==0:
                    acc.append(cur.copy())
                return
            palins = palins+[s[i]]
            if isPalindrome(palins):
                cur.append("".join(palins))
                recur(cur, [], i+1)
                cur.pop()
            recur(cur,palins,i+1)
        recur([],[],0)
        return acc