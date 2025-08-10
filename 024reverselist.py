class Node:
    # Define a Node in a linked list
    def __init__(self, val):
        self.val = val       # Store the value for this node
        self.next = None     # Pointer to the next node (default: None)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


def reverse_list(head):
    previous = None            # 'previous' will trail behind 'current'; initially, the reversed list is empty
    current = head              # Start at the head of the original linked list
    
    while current is not None:  # Continue until we reach the end of the list
        next = current.next     # Temporarily store the next node so we don't lose it
        current.next = previous # Reverse the link: point current node to the previous node
        previous = current      # Move 'previous' forward to the current node (new head of reversed list so far)
        current = next          # Move 'current' forward to the original next node
    
    return previous             # At the end, 'previous' will be the new head of the reversed list

'''
def reverse_list(head, previous=None):
    if head is None:
        return previous         # Base case: if we've gone past the last node, return the new head (previous)
    
    next = head.next            # Save the next node before breaking the link
    head.next = previous        # Reverse the link so current node points to previous
    return reverse_list(next, head)  # Recursive call: move forward to the saved 'next', 
                                     # making the current node the new 'previous'

'''