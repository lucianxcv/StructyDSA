class Node:
    # Define a Node in a linked list
    def __init__(self, val):
        self.val = val       # Store the value for this node
        self.next = None     # Pointer to the next node (default: None)

# Create 4 linked list nodes with values "a", "b", "c", and "d"
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

# Link the nodes together: a -> b -> c -> d
a.next = b
b.next = c
c.next = d

def get_node_value(head, index):
    current = head                  # Start at the head of the linked list
    count = 0                      # Initialize a counter to track the current node's position
    
    while current is not None:     # Loop through the list until we reach the end (None)
        if count == index:         # If the current position matches the target index
            return current.val     # Return the value of the current node
        
        count += 1                # Increment the position counter
        current = current.next     # Move to the next node in the list
    
    return None                   # If index is out of range, return None
print(get_node_value(a, 3))

"""
def get_node_value(head, index):
    if head is None:
        return None                  # Base case: If the list is empty or we've reached the end, return None
    
    if index == 0:
        return head.val              # Base case: If we've reached the target index, return the current node's value
    
    # Recursive step: Move to the next node and decrease index by 1
    return get_node_value(head.next, index - 1)

# How it works:
# - Checks if the current node exists. If not, returns None since index is out of range.
# - If index is 0, returns the current node
"""
