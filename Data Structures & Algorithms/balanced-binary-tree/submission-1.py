# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True
        self.height(root)
        return self.res

    def height(self,root)->int:
        if not root:
            return 0 
        l = self.height(root.left) if root.left else 0
        r = self.height(root.right) if root.right else 0
        self.res = abs(l-r) < 2 and self.res
        return max(l,r)+1



