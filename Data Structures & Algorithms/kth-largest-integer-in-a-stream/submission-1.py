class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.topk = nums
        while len(self.topk) > k:
            heapq.heappop(self.topk)        
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.topk,val)
        if len(self.topk) > self.k:
            heapq.heappop(self.topk)
        return self.topk[0]
        
