class Node:
    def __init__(self, datavalue=None):
        self.datavalue = datavalue
        self.nextvalue = None


class LinkedList:
    def __init__(self):
        self.headvalue = None

    def traverse(self):
        node = self.headvalue
        while node:
            print(node.data, end="==>")
            node = node.next


l1 = LinkedList()
l1.headvalue = Node("Head Node")
node1 = Node("Python")
node2 = Node("Java")
l1.headvalue.nextvalue = node1
l1.headvalue.nextvalue.nextvalue = node2
# print(l1)
print(l1.traverse())

l2 = LinkedList()
l2.headvalue = Node("Head Node")
node1 = Node("Python")
node2 = Node("Java")
l2.headvalue.nextvalue = node1
node1.nextvalue = node2
# print(l2)
print(l2.traverse())
