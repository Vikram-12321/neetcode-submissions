# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        self.balanced = True
        self.height(root)

        return self.balanced
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if (root.left is None) and (root.right is None):
            return 1
        
        h_l, h_r = self.height(root.left), self.height(root.right)
        diff = h_l - h_r
        if (diff < -1) or (diff > 1):
            self.balanced = False

        return 1 + max(h_l, h_r)
