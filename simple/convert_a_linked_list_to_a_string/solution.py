def stringify(node):
    res = ''
    head = node
    current = head
    while current:
        res += str(current.data) + ' -> '
        current = current.next
    return res + 'None'
