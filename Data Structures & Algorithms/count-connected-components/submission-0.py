class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.buildGraph(edges, n)
        count = 0

        visited = set()
        for node in range(n):
            if self.explore(graph, node, visited):
                count += 1
        return count
        
        
    def explore(self, graph, node, visited):
        if node in visited:
            return False
        visited.add(node)

        for neighbor in graph[node]:
            self.explore(graph, neighbor, visited)
        
        return True


    def buildGraph(self, edges, n):
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        return graph

