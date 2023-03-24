# simple BFS to check if dest is reachable from source in an undirected graph

from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        # undirected graph
        self.graph[u].append(v)
        self.graph[v].append(u)

    def hasPath(self, start, end):
        visited = [False] * self.v
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            node = queue.pop(0)
            # print(node)

            if node == end:
                # print("yes")
                return True

            for i in range(len(self.graph[node])):
                if visited[self.graph[node][i]] == False:
                    queue.append(self.graph[node][i])
                    visited[self.graph[node][i]] = True
                else:
                    continue
            # print(queue)
        return False


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        g = Graph(n)

        # add edge
        for i in range(len(edges)):
            g.addEdge(edges[i][0], edges[i][1])

        # print(g.graph)
        # check if end is reachable from the start
        return g.hasPath(start, end)
