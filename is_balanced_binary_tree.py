class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def helper(self, root):
        if root is None: 
            return -1, True
        
        left_height, is_balanced = self.helper(root.left)
        left_height += 1
        if not is_balanced:
            return left_height, False
        
        right_height, is_balanced = self.helper(root.right)
        right_height += 1
        if not is_balanced:
            return right_height, False
        
        return max(left_height, right_height), abs(left_height - right_height) <= 1
    
    def isBalanced(self, root):
        return self.helper(root)[1]

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(4)

a.left = b
a.right = c

b.left = d
b.right = e

d.left = f
d.right = g

s.isBalanced(a)