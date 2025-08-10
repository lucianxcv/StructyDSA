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

print(get_node_value(a, 1))