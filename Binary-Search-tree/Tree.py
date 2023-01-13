class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if temp.value<value:
                temp = temp.left
            elif temp.value > value:
                temp = temp.right
            else:
                return True
        return False


tree = BST()

tree.insert(2)
tree.insert(1)
tree.insert(3)

print(tree.contains(5))

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
