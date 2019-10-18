"""Check if a binary tree is subtree of another binary tree | Set 2
Given two binary trees, check if the first tree is subtree of the second one. A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T.
The subtree corresponding to the root node is the entire tree; the subtree corresponding to any other node is called a proper subtree.

For example, in the following case, Tree1 is a subtree of Tree2. """


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node, res):

    if not node:
        return

    #global res_inorder
    res.append(node.data)
    preorder(node.left, res)
    preorder(node.right, res)


root = Node('x')
root.left = Node('a')
root.right = Node('b')
root.left.right = Node('c')

sub_tree_inorder = []
preorder(root, sub_tree_inorder)

print(sub_tree_inorder)

