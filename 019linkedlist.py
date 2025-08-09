class Node:
    #constructor/initializer which will take a single argument value, always take a reference to the self as well in classes.
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b 
b.next = c 
c.next = d 

#A => B => C => D => None
#current starts at head being A,then i check, is A node not None:
#thats True so i print out A and then we make current = with curent.next which is the next node and so on
#


'''def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next
print_list(a)'''
#---------------------------Recursive way

def print_list(head):
    if head is None:
        return
    else:
        print(head.val)
        print_list(head.next)
    
print_list(a)