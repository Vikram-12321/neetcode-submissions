# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, root.val)] #node, max value on path from node to root
        res = 1
        
        while stack:
            node, max_val = stack.pop()


            if node.right:
                if node.right.val >= max_val:
                    res += 1
                    stack.append((node.right, node.right.val))
                else:
                    stack.append((node.right, max_val))

            if node.left:
                if node.left.val >= max_val:
                    res += 1
                    stack.append((node.left, node.left.val))
                else:
                    stack.append((node.left, max_val))

        return res
                    