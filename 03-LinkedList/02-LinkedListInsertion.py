class Node:
    def __init__(self, data: str = None):
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

    def insert_end(self, data: str):
        node = self.head
        new_node = Node(data)
        if not node:
            self.head = new_node
            return

        while node.next:
            node = node.next
        node.next = new_node

    def insert_beginning(self, data: str):
        node = Node(data)
        node.next = self.head
        self.head = node

    @staticmethod
    def insert_between(node: Node, data: str):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node


ll = LinkedList()

ll.head = Node("CPP")
node1 = Node("Python")
node2 = Node("Java")
ll.head.next = node1
node1.next = node2
print(ll.traverse())

ll.insert_end("Node")
print(ll.traverse())

ll.insert_end("Golang")
print(ll.traverse())

ll.insert_beginning("Dotnet")
print(ll.traverse())

ll.insert_between(ll.head.next, "Assembly")
print(ll.traverse())

ll = LinkedList()
ll.insert_end("Assembly")
print(ll.traverse())

ll = LinkedList()
ll.insert_beginning("Assembly")
print(ll.traverse())
