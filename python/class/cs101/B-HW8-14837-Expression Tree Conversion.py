class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = input().strip()

def build(a):
    if a.isdigit():
        return Node(a)
    
    if a.startswith('(') and a.endswith(')'):
        a = a[1:-1]

    depth = 0
    for i, char in enumerate(a):
        if char == "(":
            depth += 1  
        elif char == ")":
            depth -= 1
        elif depth == 0 and char in "+-/*":
            root = Node(char)

            root.left = build(a[:i])
            root.right = build(a[i+1:])
            return root

def preorder(node, out):
    if not node:
        return None
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)

def calculate(node):
    if node.val.isdigit():
        return int(node.val)

    left_value = calculate(node.left)
    right_value = calculate(node.right)

    if node.val == '+':
        return left_value + right_value
    elif node.val == '-':
        return left_value - right_value
    elif node.val == '*':
        return left_value * right_value
    elif node.val == '/':
        return left_value // right_value
output = []
strings = build(a)
preorder(strings, output)
print(' '.join(output))
print(calculate(strings))
