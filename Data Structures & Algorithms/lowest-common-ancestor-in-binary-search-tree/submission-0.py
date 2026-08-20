# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def contains(node, tar):
            if not node:
                return False
            if node.val==tar.val:
                return True
            return contains(node.left, tar) or contains(node.right, tar)

        res = root
        lis = [root]
        while len(lis) > 0:
            node = lis.pop()
            if not node:
                continue
            if contains(node, p) and contains(node, q):
                res = node
            lis.append(node.left)
            lis.append(node.right)

        return res