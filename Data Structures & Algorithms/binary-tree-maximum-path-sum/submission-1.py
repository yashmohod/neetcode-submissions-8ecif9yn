# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float("inf")
        self.dfs(root)
        return self.res

    def dfs(self, cur):
        if not cur:
            return 0
        l = max(self.dfs(cur.left), 0)   # discard negative subtrees
        r = max(self.dfs(cur.right), 0)  # discard negative subtrees
        
        self.res = max(self.res, l + r + cur.val)  # best path through cur
        
        return max(l, r) + cur.val  # return best single arm to parent
        

