class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def add_to_front(self, data):
        node = ListNode(data, self.head)
        self.head = node

    def add_to_end(self, value):
        if self.tail == None:
            self.add_to_front(value)
        else:
            last = ListNode(value, None)
            self.tail.set_next(last)
            self.tail = last

    def __str__(self):
        return str(self.head)

class ListNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def set_value(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data) + ", " + str(self.next)
