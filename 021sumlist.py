class Node:
    # Constructor/initializer for Node class
    # Takes 'val' as the value of the node
    # 'self' refers to the instance of the class being created
    def __init__(self, val):
        self.val = val       # Store the node's value
        self.next = None     # Initialize next pointer to None (no next node yet)


# Create individual nodes with values
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

# Link the nodes together to form a linked list:
# a -> b -> c -> d -> e
a.next = b
b.next = c
c.next = d
d.next = e


def sum_list(head):
    sum = 0              # Initialize sum accumulator
    current = head       # Start traversing from the head node
    while current is not None:
        sum += current.val  # Add current node's value to sum
        current = current.next  # Move to next node in the list
    return print(sum)    # Print the total sum of all node values


# Call sum_list function starting from the first node 'a'
sum_list(a)

"""
-----------------Recursive way O(n) time and Space O(n) because of the stack calls
def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)

print(sum_list(a))"""