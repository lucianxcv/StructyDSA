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

# Function to check if a target value exists in the linked list
def linked_list_find(head, target):
    current = head                    # Start traversal from the head node
    while current is not None:         # Keep going until we reach the end (None)
        if current.val == target:      # If current node's value matches target
            return True                # Found it, return True immediately
        current = current.next         # Move to the next node in the list
    return False                       # If loop finishes, target was not found

"""
-------------------------------Recursive case
def linked_list_find(head, target):
    if head is None:                   # Base case: reached end of list, target not found
        return False
    elif head.val == target:            # Base case: current node value matches target
        return True
    return linked_list_find(head.next, target)  # Recursive step: check the rest of the list
"""

# Test the function: check if "d" is in the linked list starting at 'a'
print(linked_list_find(a, "d"))  # Expected output: True