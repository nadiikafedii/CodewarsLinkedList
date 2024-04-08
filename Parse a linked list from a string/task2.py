def linked_list_from_string(s):
    if s == "None":
        return None
    values = s.split(' -> ')
    nodes = [Node(int(value)) for value in values[:-1]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]
