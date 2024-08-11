class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node

    def insert_before_node(self, node, data):
        if node is None:
            print("ERROR: 'insert_before_node'. No such node")
            return
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node

        if node.prev:
            node.prev.next = new_node
        else:
            self.head = new_node
    
        node.prev = new_node

    def insert_after_node(self, node, data):
        if node is None:
            print("ERROR: 'insert_after_node'. No such node")
            return
        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node

        if node.next:
            node.next.prev = new_node
        
        node.next = new_node

    def delete_first(self):
        if self.head is None:
            print("ERROR: 'delete_first'. List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        if self.head is None:
            print("ERROR: 'delete_last'. List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.prev.next = None

    def delete_at_index(self, index):
        if self.head is None:
            print("ERROR: 'delete_at_index'. List is empty")
            return
        if index < 0:
            print("ERROR: 'delete_at_index'. Invalid index")
            return
        if index == 0:
            self.delete_first()
            return
        cur_node = self.head
        for i in range(index):
            if cur_node is None:
                print("ERROR: 'delete_at_index'. Index out of range")
                return
            cur_node = cur_node.next
        if cur_node is None:
            print("ERROR: 'delete_at_index'. Index out of range")
            return
        if cur_node.next:
            cur_node.next.prev = cur_node.prev
        if cur_node.prev:
            cur_node.prev.next = cur_node.next
        del cur_node

    def traverse(self):
        if self.head is None:
            print("ERROR: 'delete_at_index'. List is empty")
            return
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" <-> ")
            cur_node = cur_node.next
        print("None")

