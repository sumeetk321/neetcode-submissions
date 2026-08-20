# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(node, l, r):
            if not node:
                return True
            if node.val >= r or node.val <= l:
                return False

            return validBST(node.left, l, node.val) and validBST(node.right, node.val, r)

        return validBST(root, float('-inf'), float('inf'))