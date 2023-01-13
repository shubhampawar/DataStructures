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

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.left
            elif temp.value > value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        queue = []
        result = []
        current_node = self.root
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return result

    def depth_first_search_pre_order(self):
        result = []

        def traverse(current_node):

            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result


tree = BST()

tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

print(tree.contains(5))

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
print(tree.BFS())
print(tree.depth_first_search_pre_order())
