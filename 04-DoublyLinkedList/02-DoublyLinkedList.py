from typing import Optional


class Node:
    def __init__(self, data: str):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __repr__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def add(self, data: str):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def traverse(self):
        node = self.head
        while node:
            print(node, end=" -> ")
            node = node.next


ll = LinkedList()
ll.add("Pune")
print(ll.traverse())
ll.add("Mumbai")
print(ll.traverse())
ll.add("Ahmedabad")
print(ll.traverse())
