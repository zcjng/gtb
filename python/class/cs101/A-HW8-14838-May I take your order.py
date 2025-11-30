class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

inorder = input().split()
postorder = input().split()

indexes = { a : b for b, a in enumerate(inorder)}

def tree(instart, inend, poststart, postend):
    if instart > inend:
        return None
    
    root_value = postorder[postend]
    root = Node(root_value)
    idx = indexes[root_value]

    left_size = idx - instart

    root.left = tree(instart, idx - 1, poststart, poststart + left_size - 1)
    root.right = tree(idx + 1, inend, poststart + left_size, postend - 1)

    return root

def preorder(node):
    if node is None:
        return None
    print(f'{node.value}', end=" ")
    preorder(node.left)
    preorder(node.right)

root = tree(0, len(inorder) - 1, 0, len(postorder) - 1)

preorder(root)
