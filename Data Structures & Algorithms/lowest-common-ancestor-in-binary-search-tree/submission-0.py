# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def lca(cur,ln,rn):

            

            nl,l = lca(cur.left,ln,rn) if cur.left else (None,False)
            nr,r = lca(cur.right,ln,rn) if cur.right else (None,False)

            if l and r:
                return cur,True
            if l :
                if cur.val == ln.val or cur.val == rn.val:
                    return cur, True
                
                return nl,l
            if r :
                if cur.val == ln.val or cur.val == rn.val:
                    return cur, True
                return nr,r
            
            if cur.val == ln.val or cur.val == rn.val:
                    return cur, True
            
            return None,False
        res,i = lca(root,p,q)

        return res



