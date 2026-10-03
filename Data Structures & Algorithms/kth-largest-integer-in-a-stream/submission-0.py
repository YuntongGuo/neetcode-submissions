class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_size = len(nums)
        heapq.heapify(nums)
        self.topk = nums
        while self.heap_size > k:
            heapq.heappop(self.topk)
            self.heap_size-=1
        
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.topk,val)
        self.heap_size += 1
        if self.heap_size > self.k:
            heapq.heappop(self.topk)
            self.heap_size -= 1
        return self.topk[0]
        
