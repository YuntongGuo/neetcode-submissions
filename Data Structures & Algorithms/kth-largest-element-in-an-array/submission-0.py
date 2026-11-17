class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        count = 0
        for n in nums:
            heapq.heappush(heap, n)
            count += 1
            if count> k:
                heapq.heappop(heap)
                count -= 1
        big = heapq.heappop(heap)
        return big