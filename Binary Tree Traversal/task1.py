# Pre-order traversal
def pre_order(node):
    result = []
    def traverse(n):
        if not n:
            return
        result.append(n.data)
        traverse(n.left)
        traverse(n.right)
    traverse(node)
    return result

# In-order traversal
def in_order(node):
    result = []
    def traverse(n):
        if not n:
            return
        traverse(n.left)
        result.append(n.data)
        traverse(n.right)
    traverse(node)
    return result

# Post-order traversal
def post_order(node):
    result = []
    def traverse(n):
        if not n:
            return
        traverse(n.left)
        traverse(n.right)
        result.append(n.data)
    traverse(node)
    return result
