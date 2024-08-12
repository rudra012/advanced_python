class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def traverse(self):
        node = self.head
        while node:
            print(node.data, end="==>")
            node = node.next

    def del_node(self, del_data):
        if self.head and self.head.data == del_data:
            self.head = self.head.next
            return

        node = self.head
        prev: Node = None
        while node:
            if node.data == del_data:
                break
            prev = node
            node = node.next

        prev.next = node.next


ll = LinkedList()
ll.head = Node("CPP")
node1 = Node("Python")
node2 = Node("Java")
ll.head.next = node1
ll.head.next.next = node2
print(ll.traverse())

ll.del_node("Python")
print(ll.traverse())

ll.del_node("CPP")
print(ll.traverse())
