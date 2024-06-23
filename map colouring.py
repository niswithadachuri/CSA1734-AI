def is_valid(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def backtrack(graph, colors, node, num_colors):
    if node == len(graph):
        return True
    
    for color in range(1, num_colors + 1):
        if is_valid(graph, colors, node, color):
            colors[node] = color
            if backtrack(graph, colors, node + 1, num_colors):
                return True
            colors[node] = 0
            
    return False

def map_coloring(graph, num_colors):
    colors = [0] * len(graph)
    if backtrack(graph, colors, 0, num_colors):
        return colors
    else:
        return None

# Example usage
# Graph representation: adjacency list
# 0---1
# | \ |
# 2---3
graph = [
    [1, 2, 3],  # Neighbors of node 0
    [0, 3],     # Neighbors of node 1
    [0, 3],     # Neighbors of node 2
    [0, 1, 2]   # Neighbors of node 3
]

num_colors = 3
solution = map_coloring(graph, num_colors)
if solution:
    print("Solution found:", solution)
else:
    print("No solution exists")
