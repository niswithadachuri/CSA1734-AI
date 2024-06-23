import itertools
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  
    return total_distance
def find_shortest_route(distance_matrix):
    num_cities = len(distance_matrix)
    all_permutations = itertools.permutations(range(num_cities))
    min_distance = float('inf')
    best_route = None  
    for perm in all_permutations:
        current_distance = calculate_total_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm 
    return best_route, min_distance
best_route, min_distance = find_shortest_route(distance_matrix)
print("Best route:", best_route)
print("Minimum distance:", min_distance)
