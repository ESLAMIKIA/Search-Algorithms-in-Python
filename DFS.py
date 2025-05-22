graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

##DFS

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    if start == goal:
        return True
    for neighbor in graph[start]:
        if neighbor not in visited:
            found = dfs(graph, neighbor, goal, visited)
            if found:
                return True
    return False

print("\nDFS:")
dfs(graph, 'A', 'F')