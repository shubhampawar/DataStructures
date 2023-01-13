class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def print_queue(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            self.bottom.next = new_node
            self.bottom = new_node
        self.height += 1

    def dequeue(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next
            return temp


queue = Queue(4)
queue.enqueue(33)
queue.enqueue(333)
queue.enqueue(3333)
queue.enqueue(33333)
queue.print_queue()
print("=========")
queue.dequeue()
queue.print_queue()
