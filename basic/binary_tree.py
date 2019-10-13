class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    preorder(root)

main()

