class Stack:
    
    def __init__(self, stack = None):
        self.stack = stack

    def __repr__(self):
        return str(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()