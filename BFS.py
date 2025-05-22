graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

##BFS 

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            print(node)
            return True
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return False

print("\n\nBFS:")
bfs(graph, 'A', 'F')
