from collections import deque

# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, m_right, c_right = state
    # Check that no side has more cannibals than missionaries (unless no missionaries are present)
    if m_left < c_left and m_left > 0:
        return False
    if m_right < c_right and m_right > 0:
        return False
    return True

# Function to generate all possible next states from the current state
def get_next_states(state, boat_position):
    m_left, c_left, m_right, c_right = state
    next_states = []
    
    if boat_position == "left":  # Boat on the left side
        if m_left >= 2:  # Two missionaries cross
            next_states.append((m_left - 2, c_left, m_right + 2, c_right))
        if c_left >= 2:  # Two cannibals cross
            next_states.append((m_left, c_left - 2, m_right, c_right + 2))
        if m_left >= 1 and c_left >= 1:  # One missionary and one cannibal cross
            next_states.append((m_left - 1, c_left - 1, m_right + 1, c_right + 1))
        if m_left >= 1:  # One missionary crosses
            next_states.append((m_left - 1, c_left, m_right + 1, c_right))
        if c_left >= 1:  # One cannibal crosses
            next_states.append((m_left, c_left - 1, m_right, c_right + 1))
    else:  # Boat on the right side
        if m_right >= 2:  # Two missionaries cross back
            next_states.append((m_left + 2, c_left, m_right - 2, c_right))
        if c_right >= 2:  # Two cannibals cross back
            next_states.append((m_left, c_left + 2, m_right, c_right - 2))
        if m_right >= 1 and c_right >= 1:  # One missionary and one cannibal cross back
            next_states.append((m_left + 1, c_left + 1, m_right - 1, c_right - 1))
        if m_right >= 1:  # One missionary crosses back
            next_states.append((m_left + 1, c_left, m_right - 1, c_right))
        if c_right >= 1:  # One cannibal crosses back
            next_states.append((m_left, c_left + 1, m_right, c_right - 1))
    
    return next_states

# BFS function to solve the problem
def solve_missionaries_cannibals():
    # Initial state: (missionaries_left, cannibals_left, missionaries_right, cannibals_right)
    initial_state = (3, 3, 0, 0)
    goal_state = (0, 0, 3, 3)
    
    # Queue for BFS: state, boat_position, and the path taken so far
    queue = deque([(initial_state, "left", [])])
    visited = set()

    while queue:
        state, boat_position, path = queue.popleft()

        if state == goal_state:  # Check if the goal state is reached
            print("Solution found:")
            for step in path + [(state, boat_position)]:
                print(f"State: {step[0]}, Boat: {step[1]}")
            return

        # Mark state as visited
        if (state, boat_position) in visited:
            continue
        visited.add((state, boat_position))

        # Generate the next possible states
        next_boat_position = "right" if boat_position == "left" else "left"
        for next_state in get_next_states(state, boat_position):
            if is_valid(next_state) and (next_state, next_boat_position) not in visited:
                queue.append((next_state, next_boat_position, path + [(state, boat_position)]))

    print("No solution found.")

# Example usage
solve_missionaries_cannibals()
