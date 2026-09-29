# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        


        if root == subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            l = root.left == subRoot.left or self.isSubtree(root.left,subRoot.left)
            r = root.right == subRoot.right or self.isSubtree(root.right,subRoot.right)
            return l and r
        else:
            l = root.left == subRoot or self.isSubtree(root.left,subRoot)
            r = root.right == subRoot or self.isSubtree(root.right,subRoot)
            return l or r

        


