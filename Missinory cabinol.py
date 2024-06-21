from collections import deque

initial_state = (3, 3, 0, 0, 1)  

goal_state = (0, 0, 3, 3, 0)

moves = [
    (1, 0),  
    (2, 0),  
    (0, 1),  
    (0, 2), 
    (1, 1)  
]

def is_valid_state(state):
    m_left, c_left, m_right, c_right, _ = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_next_states(state):
    m_left, c_left, m_right, c_right, boat_position = state
    next_states = []
    
    for move in moves:
        if boat_position == 1:  
            new_state = (m_left - move[0], c_left - move[1], m_right + move[0], c_right + move[1], 0)
        else:  
            new_state = (m_left + move[0], c_left + move[1], m_right - move[0], c_right - move[1], 1)
        
        if is_valid_state(new_state):
            next_states.append(new_state)
    
    return next_states

def solve():
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [current_state]
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        for next_state in get_next_states(current_state):
            queue.append((next_state, path + [current_state]))
    
    return None
solution = solve()

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
