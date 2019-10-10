# Ideally I will be able to solve the subset sum problem

# Two implementations: solving it first, and solving every way

nums = [1, 2, 3, 4, 12, 45, 95, 102]

path = []


# Having a linked list where we contain each possible outcome
# the back tracking will just go back through til something is not included and then if its not drop it

class LinkedList:
    def __init__(self, include, value, n):
        self.include = include
        self.value = value
        self.next = n

    def setNext(n):
        self.next = n
