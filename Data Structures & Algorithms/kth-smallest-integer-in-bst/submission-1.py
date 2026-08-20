# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        d = dict()
        def size(node):
            if not node:
                return 0
            val = 1+size(node.left)+size(node.right)
            d[node] = val
            return val
        size(root)
        def solve(node, tar):
            if node.left and d[node.left] > 0:
                if d[node.left] < tar:
                    tar -= d[node.left]
                    d[node.left] = 0
                    return solve(node, tar)
                else:
                    return solve(node.left, tar)
            elif node.right and d[node.right] > 0:
                if tar==1:
                    return node.val
                return(solve(node.right, tar-1))
            return node.val
        return solve(root, k)


        
