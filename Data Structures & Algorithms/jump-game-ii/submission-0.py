class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        edge = 0
        end = 0
        for i in range(len(nums)-1):
            edge = max(edge,i + nums[i])
            if i == end:
                count += 1
                end = edge
        return count