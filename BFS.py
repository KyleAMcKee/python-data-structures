class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, item):
        new_item = Node(item)
        if not self.first:
            self.first = self.last = new_item
        else:
            self.last.next = new_item
            self.last = new_item

    def dequeue(self):
        if self.first:
            ret = self.first
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return ret.item
    
    def is_empty(self):
        if self.first is None:
            return True
        return False



def level_order_traversal(root):

    q = Queue()
    q.enqueue(root)
    while (not q.is_empty()):
        
        curr = q.dequeue()
        print(curr.value)
        
        if curr.left:
            q.enqueue(curr.left)
        if curr.right:
            q.enqueue(curr.right)


a = TreeNode(8)
b = TreeNode(9)
c = TreeNode(12)
d = TreeNode(14)
e = TreeNode(10)
f = TreeNode(7)
g = TreeNode(11)
h = TreeNode(6)

a.left = b
a.right = g
b.left = c
b.right = d
d.left = e
e.right = f
g.left = h

level_order_traversal(a)
