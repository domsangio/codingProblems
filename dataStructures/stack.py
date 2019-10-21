class Stack:
    
    def __init__(self, stack = []):
        self.stack = stack
        self.size = 0

    def __repr__(self):
        return str(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.pop()