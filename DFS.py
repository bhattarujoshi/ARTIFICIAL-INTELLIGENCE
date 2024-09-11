from collections import deque

# Node class representing a tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to perform DFS on a binary tree (iterative)
def dfs_iterative(root):
    if root is None:
        return
    
    # Stack to simulate recursive DFS behavior
    stack = [root]
    
    while stack:
        # Pop a node from the top of the stack
        node = stack.pop()
        print(node.value, end=" ")
        
        # Push right child first so the left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Function to create the binary tree by taking input from the user
def create_tree():
    # Helper function to create nodes
    def add_node(value):
        if value == '':  # If the input is empty, return None
            return None
        return Node(int(value))
    
    # Input the value for the root node
    root_value = input("Enter the value for the root node: ")
    root = add_node(root_value)
    
    # Queue to build the tree level by level
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()
        
        if current_node:
            # Input the value for the left child
            left_value = input(f"Enter the left child of {current_node.value} (leave blank if no child): ")
            current_node.left = add_node(left_value)
            if current_node.left:
                queue.append(current_node.left)
            
            # Input the value for the right child
            right_value = input(f"Enter the right child of {current_node.value} (leave blank if no child): ")
            current_node.right = add_node(right_value)
            if current_node.right:
                queue.append(current_node.right)
    
    return root

# Example usage
# Create the tree by taking input from the user
root = create_tree()

# Perform DFS (Iterative) on the binary tree
print("\nDFS traversal (iterative) of the tree:")
dfs_iterative(root)
