class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        target = Counter(t)
        count = len(t)
        shortest = len(s)+1
        shortest_str = ""
        l = 0
        for r in range(len(s)):
            if s[r] in target:
                target[s[r]] -= 1
                if target[s[r]] >= 0:
                    count -= 1
                if count == 0:
                    # print(s[l:r+1])
                    while count == 0:
                        if s[l] in target:
                            target[s[l]] += 1
                            if target[s[l]] > 0:
                                count += 1
                        l+=1
                    # print(s[l-1:r+1])
                    if r-(l-1)+1 < shortest:
                        shortest = r-(l-1)+1
                        shortest_str = s[l-1:r+1]
        return shortest_str