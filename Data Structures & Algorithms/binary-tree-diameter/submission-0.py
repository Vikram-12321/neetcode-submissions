# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self.depth(root)
        return self.best

    def depth(self,root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        d_l, d_r = self.depth(root.left), self.depth(root.right)
        
        self.best = max(self.best, d_l + d_r) ## Best Calculation

        return 1 + max(d_l, d_r)
        

