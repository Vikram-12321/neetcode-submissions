# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None) and (subRoot is None):
            return True
        
        elif (root is None) or (subRoot is None):
            return False
        
        ## Root == SubRoot
        if root.val == subRoot.val:
            c = self.isIdentical(root, subRoot)
            if c:
                return True

        ## subroot is lower down
        c_l = self.isSubtree(root.left, subRoot) 
        c_r = self.isSubtree(root.right, subRoot) 
        return c_l or c_r
    
    def isIdentical(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) and (q is None):
            return True
        if (p is None) or (q is None):
            return False
        
        if p.right is None and p.left is None:
            if q.right is None and q.left is None:
                return p.val == q.val
            return False

        if q.right is None and q.left is None:
            if p.right is None and p.left is None:
                return p.val == q.val
            return False

        l, r = self.isIdentical(p.left, q.left), self.isIdentical(p.right, q.right)

        if l and r and p.val == q.val:
            return True

        return False