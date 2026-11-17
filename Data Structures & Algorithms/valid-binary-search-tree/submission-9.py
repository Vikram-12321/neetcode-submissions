# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, [float('-inf'), float('inf')])]

        while stack:
            node, interval = stack.pop()

            if not node:
                break

            if node.right:
                if node.right.val > node.val and node.right.val < interval[1]:
                    stack.append((node.right, [node.val, interval[1]]))
                else:
                    return False

            if node.left:
                if node.left.val < node.val and node.left.val > interval[0]:
                    stack.append((node.left, [interval[0], node.val]))
                else:
                    return False

        return True
