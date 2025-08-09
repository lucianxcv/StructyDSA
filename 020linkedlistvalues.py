# Define a Node class for our linked list
class Node:
    def __init__(self, val):
        self.val = val       # Store the node's value
        self.next = None     # Pointer to the next node (None means no next node yet)

# Create individual nodes
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

# Link the nodes together to form the list: a -> b -> c -> d
a.next = b
b.next = c
c.next = d

# Main function to get all values from a linked list
def linked_list_values(head):
    values = []                 # Start with an empty list to store the values
    fill_values(head, values)   # Call helper function to fill the list recursively
    return values               # Return the completed list of values

# Helper recursive function to traverse the linked list
def fill_values(head, values):
    if head is None:            # Base case: if we reach the end (no more nodes)
        return                   # Stop recursion
    values.append(head.val)     # Add the current node's value to the list
    fill_values(head.next, values)  # Recurse with the next node in the list

# Run the function starting from the head node 'a' and print the result
print(linked_list_values(a))     # Output: ['a', 'b', 'c', 'd']

"""
-----------------------Iterative way-------------------------Non Recursive way:
def linked_list_values(head):
    values = []          # Start with empty list
    current = head       # Begin with the head node
    while current is not None:  # Loop until you reach the end
        values.append(current.val)  # Add current node's value
        current = current.next       # Move to next node
    return values        # Return collected values
    """