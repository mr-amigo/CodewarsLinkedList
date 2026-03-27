class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next
    first.next = swap_pairs(second.next)
    second.next = first
    return second
