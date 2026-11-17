class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph
        graph = defaultdict(list)
        for p in prerequisites:
            source = p[0]
            target = p[1]
            graph[source].append(target)
        sequence = []
        valid = set()
        def dfs(node,visited):
            if node in visited:
                return False
            if node in valid:
                return True
            requires = graph[node]
            if len(requires) == 0:
                sequence.append(node)
                valid.add(node)
                return True
            visited.add(node)
            for p in graph[node]:
                if not dfs(p,visited):
                    return False
            sequence.append(node)
            valid.add(node)
            visited.discard(node)
            return True
        for i in range(numCourses):
            if i not in valid:
                validity = dfs(i,set())
                if not validity:
                    return []
        
        return sequence
