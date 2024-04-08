def stringify(node):
    if node is None:
        return "None"
    else:
        return str(node.data) + " -> " + stringify(node.next)