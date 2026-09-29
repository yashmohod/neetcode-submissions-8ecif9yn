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

    def dfs(self,cur):
        if not cur:
            return 0
        l = self.dfs(cur.left) 
        r = self.dfs(cur.right) 
        self.res = max(self.res, l+ cur.val)
        self.res = max(self.res, r+ cur.val)
        self.res = max(self.res, r+l+ cur.val)
        return max(l+ cur.val,r+ cur.val)
        

