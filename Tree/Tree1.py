class Node:
    #creating a structure for the nodde
    #initializing the node's data upon calling it's constructor
    def __init__(self,data):
        self.data=data
        self.right=self.left=None
#Defining class for binary tree
class BinaryTree:
    
    def __init__(self):
        self.root=None
        
#main method
if __name__ == "__main__":
    tree=BinaryTree()
    tree.root=Node(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)

