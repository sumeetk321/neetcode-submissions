# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        d = dict()
        maxlevel = 0
        def dfs(node, level):
            nonlocal maxlevel
            if not node:
                return
            maxlevel = max(maxlevel, level)
            if level not in d.keys():
                d[level] = []
            d[level].append(node)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)

        res = []
        for k in range(maxlevel+1):
            res.append(d[k][-1].val)
        return res
