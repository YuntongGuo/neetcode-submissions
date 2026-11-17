class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct graph
        adj = defaultdict(list)
        indeg = [0] * numCourses 
        for course, pre in prerequisites:
            adj[pre].append(course)
            indeg[course] += 1
        output = []
        def dfs(node):
            indeg[node] = -1
            output.append(node)
            for course in adj[node]:
                indeg[course] -= 1
                if indeg[course] == 0:
                    dfs(course)
        for i in range(numCourses):
            if indeg[i] == 0:
                dfs(i)
        return output if len(output) == numCourses else []