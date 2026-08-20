# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def getHeight(r):
            if not r:
                return 0
            return max(getHeight(r.left), getHeight(r.right))+1
        def dfs(node, height, l):
            if not node:
                return 
            l[height].append(node.val)
            dfs(node.left, height+1, l)
            dfs(node.right, height+1,l)
        l = [[] for i in range(getHeight(root))]
        dfs(root, 0, l)
        return l