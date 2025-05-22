import heapq

weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

##UCS

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start)]  # (cost, node)
    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            print(f"Reached {goal} with cost {cost}")
            return True
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))
    return False

print("\n\nUCS:")
ucs(weighted_graph, 'A', 'F')