class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, val):
        if val < self.value:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        elif val > self.value:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
    
    @classmethod
    def print_tree(cls, node):
        if node.left:
            cls.print_tree(node.left)
        print(node.value)
        if node.right:
            cls.print_tree(node.right)
    
    def __str__(self, depth=0):
        ret = ''

        # Print right branch
        if self.right:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += '\n' + (' ____'*depth) + str(self.value)

        # Print left branch
        if self.left:
            ret += self.left.__str__(depth + 1)

        return ret
        



if __name__ == '__main__':
    tree = TreeNode(4)
    for i in [5, 3, 1, 2, 8, 7, 4]:
        tree.insert(i)

    TreeNode.print_tree(tree)

    # TreeNode.print_levels(tree)
    print(tree)
