# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if (root.left is None) and (root.right is None):
            return 1
        
        h_l = self.height(root.left)
        if h_l == -1:
            return -1

        h_r = self.height(root.right)
        if h_r == -1:
            return -1

        diff = h_l - h_r

        if (diff < -1) or (diff > 1):
            return -1

        return 1 + max(h_l, h_r)
