# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == q:
            return True 
        if not p or not q:
            return False
        
        l = q.left == p.left or self.isSameTree(q.left,p.left)
        r = q.right == p.right or self.isSameTree(q.right,p.right)

        return l and r and q.val == p.val


            