# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        elif (p.right is None) and (p.left is None):
            if (q.right is None) and (q.left is None):
                if p.val == q.val:
                    return True
            return False
        
        elif (q.right is None) and (q.left is None):
            if (p.right is None) and (p.left is None):
                if p.val == q.val:
                    return True
            return False

        e_l, e_r = self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)
        if e_l and e_r and p.val == q.val:
            return True

        return False


