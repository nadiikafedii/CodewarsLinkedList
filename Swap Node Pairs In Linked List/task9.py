from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    dummy = Node()
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next