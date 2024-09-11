# Vacuum Cleaner Agent

# Define the environment (2x2 grid for simplicity)
# 0 represents a clean space, 1 represents a dirty space
environment = [
    [1, 0],  # 1 means dirty, 0 means clean
    [0, 1]
]

# Initial position of the vacuum cleaner
vacuum_position = (0, 0)

# Function to print the current state of the environment
def print_environment(env):
    for row in env:
        print(row)
    print()

# Function to check if the grid is completely clean
def is_clean(env):
    for row in env:
        if 1 in row:
            return False
    return True

# Function to move the vacuum cleaner
def move_vacuum(position, direction):
    x, y = position
    if direction == 'up' and x > 0:
        return (x - 1, y)
    elif direction == 'down' and x < len(environment) - 1:
        return (x + 1, y)
    elif direction == 'left' and y > 0:
        return (x, y - 1)
    elif direction == 'right' and y < len(environment[0]) - 1:
        return (x, y + 1)
    return position  # No movement if out of bounds

# Vacuum cleaner agent
def vacuum_cleaner_agent():
    global vacuum_position

    # Simple vacuum cleaner logic: Clean current position if dirty, then move
    steps = 0
    while not is_clean(environment):
        x, y = vacuum_position

        # Clean the current position if it's dirty
        if environment[x][y] == 1:
            print(f"Vacuum cleaner is cleaning position {vacuum_position}")
            environment[x][y] = 0
            print_environment(environment)

        # Move to the next position (cycle through directions)
        # The vacuum cleaner will try to move right, down, left, up in a loop
        if steps % 4 == 0:
            vacuum_position = move_vacuum(vacuum_position, 'right')
        elif steps % 4 == 1:
            vacuum_position = move_vacuum(vacuum_position, 'down')
        elif steps % 4 == 2:
            vacuum_position = move_vacuum(vacuum_position, 'left')
        else:
            vacuum_position = move_vacuum(vacuum_position, 'up')

        steps += 1

    print("All positions are clean now!")

# Example usage
print("Initial Environment:")
print_environment(environment)
vacuum_cleaner_agent()
