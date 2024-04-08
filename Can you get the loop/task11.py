def loop_size(node):
    tortoise = hare = node
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return count_loop_length(tortoise)
    return 0

def count_loop_length(node):
    current = node.next
    length = 1
    while current != node:
        length += 1
        current = current.next
    return length

def create_chain(total_nodes, loop_size):
    nodes = [Node() for _ in range(total_nodes)]
    for i, node in enumerate(nodes):
        next_index = (i + 1) % total_nodes
        node.next = nodes[next_index]
    loop_start_index = total_nodes - loop_size
    nodes[-1].next = nodes[loop_start_index]
    return nodes[0]