class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while node:
            print(node.data, end="==>")
            node = node.next


ll = LinkedList()
ll.head = Node("CPP")
node1 = Node("Python")
node2 = Node("Java")
ll.head.next = node1
ll.head.next.next = node2
# print(l1)
print(ll.traverse())

ll2 = LinkedList()
ll2.head = Node("CPP")
node1 = Node("Python")
node2 = Node("Java")
ll2.head.next = node1
node1.next = node2
# print(l2)
print(ll2.traverse())
