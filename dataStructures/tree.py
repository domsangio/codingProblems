class TreeNode:
    # immutable tree nodes
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        str(self.value)

    def __str__(self):
        str(self.left) + ", " + str(self.value) + ", " + str(self.right)

class Tree:
    def __init__(self, root = None):
        self.root = root

    def __repr__(self):
        str(self.root)

    def __str__(self):
        str(self.root)

    def add_node(self, value):
        if (self.root == None):
            self.root = TreeNode(value)
            return True
        else:
            self._add_recurse_helper(value, self.root)
            return True
    
    def _add_recurse_helper(self, value, node):
        if (value == node.value):
            return True
        elif (value > node.value):
            if (node.right == None):
                node.right = TreeNode(value)
                return True
            else:
                return self._add_recurse_helper(value, node.right)
        else:
            if (node.left == None):
                node.left = TreeNode(value)
                return True
            else:
                return self._add_recurse_helper(value, node.left)
