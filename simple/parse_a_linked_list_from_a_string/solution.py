class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

stop_iteration_words = ["null", "NULL", "nil", "nullptr", "null()", "None"]

def linked_list_from_string(list_repr: str) -> Node | None:
    list_repr = list_repr.strip().split(' -> ')

    if list_repr[0] in stop_iteration_words:
        return None

    list_repr = iter(list_repr)
    head = Node(int(next(list_repr)))
    current = head

    for el in list_repr:
        if el in stop_iteration_words:
            return head
        current.next = Node(int(el.strip()))
        current = current.next
    return head
