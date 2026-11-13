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
        
        h_l, h_r = self.height(root.left), self.height(root.right)
        diff = h_l - h_r

        if (self.isBalanced(root.left) is False) or (self.isBalanced(root.right) is False):
            return False

        if (diff >= -1) and (diff <= 1):
            return True
        return False
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if (root.left is None) and (root.right is None):
            return 1
        
        h_l, h_r = self.height(root.left), self.height(root.right)

        return 1 + max(h_l, h_r)
