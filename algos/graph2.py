from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * len(self.graph)

        queue = []
        
        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.pop(0)
            
            print(s, end=' ')

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

    def dfs(self, s):
        visited = [False] * len(self.graph)

        self.dfs_util(s, visited)

    def dfs_util(self, v, visited):
        visited[v] = True

        print(v, end= ' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    for i in range(4):
        print ('Following is Breadth First Traversal (starting from vertex {})'.format(i))
        g.bfs(i)
        print('\n')

        print ('Following is Depth First Traversal (starting from vertex {})'.format(i))
        g.dfs(i)
        print('\n--------------------------------------------------------------------------')
        

    