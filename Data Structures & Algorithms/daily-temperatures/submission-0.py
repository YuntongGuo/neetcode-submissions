class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        record = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                old, cold = stack.pop()
                record[old] = i-old
            stack.append((i,t))
        return record