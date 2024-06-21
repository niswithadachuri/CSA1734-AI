from collections import deque
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [
    (-1, 0),  
    (1, 0),   
    (0, -1),  
    (0, 1)   
]

def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def create_new_state(state, move):
    x, y = find_empty_tile(state)
    new_x, new_y = x + move[0], y + move[1]

    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state
    return None
def solve_puzzle(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        visited.add(tuple(map(tuple, state)))

        if state == goal_state:
            return path

        for move in moves:
            new_state = create_new_state(state, move)
            if new_state and tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [new_state]))

    return None
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

solution = solve_puzzle(initial_state)

if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
