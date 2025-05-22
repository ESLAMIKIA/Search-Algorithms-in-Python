graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

##IDS
def dls(graph, start, goal, limit, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    if start == goal:
        return True
    if limit <= 0:
        return False
    for neighbor in graph[start]:
        if neighbor not in visited:
            found = dls(graph, neighbor, goal, limit - 1, visited)
            if found:
                return True
    return False

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth limit: {depth}")
        if dls(graph, start, goal, depth):
            return True
    return False


print("\n\nIDS:")
ids(graph, 'A', 'F', 4)