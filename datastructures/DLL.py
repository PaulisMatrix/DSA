class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def addStart(self, val):
        if self.head == None:
            self.head = Node(val)
            self.prev = None
            self.next = None
        else:
            node = Node(val)
            node.next = self.head
            node.prev = None
            self.head = node

    def addEnd(self, val):

        node = Node(val)
        if self.head == None:
            self.head = node
            node.prev = node.next = None
            # print("list is empty")

        else:
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = node
            node.prev = cur
            node.next = None

    def traverse(self):
        if self.head == None:
            print("List is empty")

        else:
            cur = self.head
            while cur:
                print(cur.data, end="->")
                cur = cur.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    # dll.traverse()

    dll.addEnd(1)
    dll.addStart(2)
    dll.addEnd(3)
    dll.addStart(10)
    dll.addEnd(100)

    dll.traverse()
