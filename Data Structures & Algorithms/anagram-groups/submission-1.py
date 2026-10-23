class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anams = defaultdict(list)
        for s in strs:
            encoded = ''.join(sorted(s))
            anams[encoded].append(s)
        return list(anams.values())
