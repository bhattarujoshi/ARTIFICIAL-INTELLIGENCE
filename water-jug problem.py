from collections import deque

def is_solvable(x, y, z):
    # If the target amount z is greater than the sum of both jugs, it's impossible
    if z > x + y:
        return False
    # If the target amount z is 0 or equal to one of the jugs, it's possible
    if z == 0 or z == x or z == y or z == x + y:
        return True
    # The problem is solvable if z is a multiple of the greatest common divisor of x and y
    return z % gcd(x, y) == 0

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def water_jug_bfs(x, y, z):
    # Initialize the queue for BFS
    queue = deque([(0, 0)])  # (jug1, jug2)
    visited = set()

    while queue:
        jug1, jug2 = queue.popleft()

        # If we find the solution
        if jug1 == z or jug2 == z or jug1 + jug2 == z:
            print(f"Solution found: ({jug1}, {jug2})")
            return True

        # Mark the current state as visited
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Possible states (operations)
        states = [
            (x, jug2),  # Fill jug1
            (jug1, y),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, y - jug2), jug2 + min(jug1, y - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(jug2, x - jug1), jug2 - min(jug2, x - jug1))   # Pour jug2 -> jug1
        ]

        # Enqueue valid states
        for state in states:
            if state not in visited:
                queue.append(state)

    print("No solution found.")
    return False

# Input from the user
x = int(input("Enter the capacity of jug1: "))
y = int(input("Enter the capacity of jug2: "))
z = int(input("Enter the target amount of water: "))

if is_solvable(x, y, z):
    water_jug_bfs(x, y, z)
else:
    print("No solution possible.")
