class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    if index < 0:
        raise IndexError()
    current = node

    for _ in range(index):
        if current is None or current.next is None:
            raise IndexError
        current = current.next
    if current is None:
        raise IndexError
    return current
