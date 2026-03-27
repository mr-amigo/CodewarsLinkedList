class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError()

    first = None
    second = None
    current = head
    toggle = True

    while current is not None:
        next_node = current.next
        if toggle:
            current.next = first
            first = current
        else:
            current.next = second
            second = current
        toggle = not toggle
        current = next_node

    first = reverse(first)
    second = reverse(second)

    return Context(first, second)

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
