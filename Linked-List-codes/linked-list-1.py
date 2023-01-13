class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_item(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop_item(self):
        if self.length < 1:
            return

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend_item(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        temp = self.head
        self.head = new_node
        new_node.next = temp
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return
        else:
            temp = self.head
            self.head = None
            self.head = temp.next
            self.length -= 1

    def get_item(self, index):
        if 0 > index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        if 0 > index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def insert_item(self, index, item):
        if 0 > index >= self.length:
            return None
        temp = self.head
        new_node = Node(item)
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def remove_item(self, index, item):
        if 0 > index >= self.length:
            return None

        pre = self.head
        for _ in range(index - 1):
            pre = pre.next
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1

    def reverse_list(self):
        if not self.length:
            return None

        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


Linkedlist = LinkedList(4)
Linkedlist.append_item(3)
Linkedlist.append_item(5)

Linkedlist.print_linked_list()
print("------------------")
Linkedlist.pop_item()
Linkedlist.print_linked_list()

print("------------------")
Linkedlist.append_item(5)
Linkedlist.prepend_item(10)
Linkedlist.print_linked_list()

print("------------------")
Linkedlist.pop_first()
Linkedlist.print_linked_list()
# print(Linkedlist.head.next.value)

print("------------------")
print(Linkedlist.get_item(2))

print("------------------")
print(Linkedlist.set_value(2, 26))
Linkedlist.print_linked_list()

print("------------------")
Linkedlist.insert_item(1, 33)
Linkedlist.print_linked_list()

print("------------------")
Linkedlist.remove_item(1, 33)
Linkedlist.print_linked_list()

print("------------------")
Linkedlist.reverse_list()
Linkedlist.print_linked_list()
