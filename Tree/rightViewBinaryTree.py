from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None
class RightView:
    def __init__(self):
        self.root=None
    def rightView(self,root):
        result=[]
        if root is None:
            return result
        queue=deque([])
        queue.append(self.root)
        while len(queue)!=0:
            level_size=len(queue)
            for i in range(level_size):
                curruuuu
        
if __name__ == '__main__':
    tree = RightView()
    tree.root = Node(12);
    tree.root.left = Node(7);
    tree.root.right = Node(1);
    tree.root.left.left = Node(9);
    tree.root.right.left = Node(10);
    tree.root.right.right = Node(5);
    tree.root.left.left.left = Node(3);
    ans = tree.rightView(tree.root)
    for node in ans:
        print(node, end = " ")
    print()