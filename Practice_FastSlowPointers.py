# GROKKING - FAST & SLOW POINTERS

# LINKED LIST CYCLE
# Determine if the linked list has a cycle

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        # Fast will move 2 steps...
        fast = fast.next.next
        # ...Everytime slow moves 1 step
        slow = slow.next
        if slow == fast:
            # A cycle has been found
            return True 
    return False

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

main()

# Time Complexity - O(N)
# Space Complexity - O(1)


##########################################################################################

# LINKED LIST CYCLE LENGTH
# Determine the length of the cycle

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# First determine if a cycle exists
def find_cycle_length(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return calculate_cycle_length(slow)
    
    return 0


# Using the location of the slow pointer, iterate through the whole cycle
# with a second pointer, until the two meet, giving us the length of the cycle
def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

main()

# Time Complexity - O(N)
# Space Complexity - O(1)


##########################################################################################

