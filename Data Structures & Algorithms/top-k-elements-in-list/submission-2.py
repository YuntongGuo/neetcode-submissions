class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        h = []
        s = 0
        for key,v in count.items():
            heapq.heappush(h,(v,key))
            s += 1
            while s > k:
                heapq.heappop(h)
                s -= 1
            # print(h)
        out = []
        while h:
            v,key = heapq.heappop(h)
            out.append(key)
        return out