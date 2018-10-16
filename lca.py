def find_level(node):
    res = 0
    while node.parent:
        res += 1
        node = node.parent

    return res