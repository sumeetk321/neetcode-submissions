# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathmap = dict()
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return (float('-inf'), float('-inf'))
            
            l = dfs(node.left)
            r = dfs(node.right)
            pathmap[node] = (max(node.val, node.val+max(l[0], l[1])), max(node.val, node.val+max(r[0], r[1])))
            print(node.val, pathmap[node])
            res = max(res, max(pathmap[node]), sum(pathmap[node])-node.val)
            return pathmap[node]
        dfs(root)
        return res


            