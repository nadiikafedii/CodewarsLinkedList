class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def reverse_list(current, prev):
        if current is None:
            return prev
        next_node = current.next
        current.next = prev
        return reverse_list(next_node, current)
    if head is None or head.next is None:
        return head
    else:
        return reverse_list(head, None)