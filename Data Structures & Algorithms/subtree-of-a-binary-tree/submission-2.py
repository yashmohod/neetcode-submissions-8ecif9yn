# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        m = self.isSameTree(root,subRoot) if root else False
        l = self.isSubtree(root.left,subRoot) if root.left else False
        r = self.isSubtree(root.right,subRoot) if root.right else False

        return m or l or r 

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == q:
            return True 
        if not p or not q:
            return False
        
        l = q.left == p.left or self.isSameTree(q.left,p.left)
        r = q.right == p.right or self.isSameTree(q.right,p.right)

        return l and r and q.val == p.val


        


