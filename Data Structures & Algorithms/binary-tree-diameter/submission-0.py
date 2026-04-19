# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0 
        self.dia(root)
        return self.res

    def dia(self,cur):
        if not cur :
            return 0 
        l = self.dia(cur.left) if cur.left else 0
        r = self.dia(cur.right) if cur.right else 0
        self.res = max(self.res,l+r)
        return max(l,r)+1
