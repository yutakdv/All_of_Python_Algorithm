# CHeck whether Graph is Bipartite or Not Using BFS

# A Bipartite Graph is a graph whose vertices can be divided into two independent sets,
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex
# from V to U. In other words, for every edge (u, v), either u belongs to U and v to V,
# or u belongs to V and v to U. We can also say that there is no edge that connects
# vertices of same set.

from queue import Queue

def check_bipartite(graph):
    queue = Queue()
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def bfs():
        while not queue.empty():
            u = queue.get()
            visited[u] = True

            for neighbor in graph[u]:
                if neighbor == u:
                    return False
                
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[u]
                    queue.put(neighbor)
                elif color[neighbor] == color[u]:
                    return False
        return True
    
    for i in range(len(graph)):
        if not visited[i]:
            queue.put(i)
            color[i] = 0
            if bfs() is False:
                return False
    
    return True

if  __name__ == "__main__":
    # Adjacency List of graph
    print(check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}))