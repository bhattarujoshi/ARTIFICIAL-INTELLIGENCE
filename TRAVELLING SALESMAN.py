from itertools import permutations

# Function to calculate the total distance of a given route
def calculate_route_distance(route, distance_matrix):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    # Add distance to return to the starting city
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

# Function to find the shortest route using brute force
def tsp_brute_force(distance_matrix):
    cities = list(range(len(distance_matrix)))  # List of cities (0, 1, 2, ..., n-1)
    shortest_route = None
    min_distance = float('inf')
    
    # Generate all possible routes (permutations of cities)
    for route in permutations(cities):
        # Calculate the total distance of the current route
        current_distance = calculate_route_distance(route, distance_matrix)
        
        # Update the minimum distance and shortest route if current route is better
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = route
            
    return shortest_route, min_distance

# Example usage
# Distance matrix representing distances between cities
distance_matrix = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

# Solve the TSP using brute force
shortest_route, min_distance = tsp_brute_force(distance_matrix)

# Display the results
print("Shortest route:", shortest_route)
print("Minimum distance:", min_distance)
