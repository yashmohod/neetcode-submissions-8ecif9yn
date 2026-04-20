# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root :
            return 0

        return self.gn(root,[])

    def gn(self,root,upto):
        f = True
        for i in upto:
            if i > root.val:
                f = False
        upto.append(root.val)     
        l = self.gn(root.left,upto) if root.left else 0
        r = self.gn(root.right,upto) if root.right else 0
        upto.remove(root.val)
        m = 1 if f else 0
        return  l+r+m