from collections import deque

def is_goal(state, target):
    return state[0] == target or state[1] == target

def get_next_states(state, capacities):
    jug1, jug2 = state
    cap1, cap2 = capacities
    next_states = []
 
    next_states.append((cap1, jug2))
  
    next_states.append((jug1, cap2))
 
    next_states.append((0, jug2))
  
    next_states.append((jug1, 0))
  
    pour_to_jug2 = min(jug1, cap2 - jug2)
    next_states.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
  
    pour_to_jug1 = min(jug2, cap1 - jug1)
    next_states.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
    
    return next_states

def solve_water_jug(capacities, target):
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        
        if is_goal(state, target):
            return path + [state]

        for next_state in get_next_states(state, capacities):
            if next_state not in visited:
                queue.append((next_state, path + [state]))

    return None


capacities = (3, 5)

target = 4


solution = solve_water_jug(capacities, target)

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
