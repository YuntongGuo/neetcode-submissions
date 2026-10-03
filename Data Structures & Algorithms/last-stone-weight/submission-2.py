class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stone = [-i for i in stones]
        heapq.heapify(neg_stone)

        while len(neg_stone) > 1:
            x = -heapq.heappop(neg_stone)
            y = -heapq.heappop(neg_stone)
            # print(x,y)
            if x > y:
                x,y = y,x
            if y - x > 0:
                heapq.heappush(neg_stone, -(y-x))
        return -neg_stone[0] if len(neg_stone) !=0 else 0