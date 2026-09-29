# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root :
            return True
        
        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)

        lv = root.val > root.left.val if root.left else True
        rv = root.val < root.right.val if root.right else True

        return (lv and rv) and l and r
