class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def search(self, node, x):
        while node:
            if node.data == x:
                return True
            if x < node.data:
                node = node.left
            else:
                node = node.right
        return False
    
    def insert(self, node, x):
        if node is None:
            return Node(x)
        elif x == node.data:
            return node
        elif x < node.data:
            node.left = node.insert(node.left, x)
        else:
            node.right = node.insert(node.right, x)
        return node

n = Node(1)
print(n.search(n, 2))
i = n.insert(n, 3)
print(i.data)
print(n.search(n, 3))