class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def printstack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push_(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop_(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next
            return temp

stacks = Stack(5)


stacks.push_(55)

stacks.push_(555)

stacks.printstack()
print("-------------------")
stacks.pop_()

stacks.printstack()

