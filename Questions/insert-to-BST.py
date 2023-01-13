class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # new_node = Node(value)
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def pre_order(self):
        ans = []

        def traverse(node):
            ans.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)

        traverse(self.root)
        return ans


tree = BST()

tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(9)
# print(tree.contains(5))

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
print(tree.pre_order())
