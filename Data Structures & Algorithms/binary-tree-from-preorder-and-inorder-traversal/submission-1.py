# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder)<=0:
            return None
        if len(preorder)<=1: 
            return TreeNode(preorder[0])

        
        rootVal = preorder[0]
        rootIdx = inorder.index(rootVal)

        inOrderLeft = inorder[:rootIdx]
        inOrderRight = inorder[rootIdx+1:]

        preOrderLeft = [x for x in preorder if x in inOrderLeft]
        preOrderRight = [x for x in preorder if x in inOrderRight]
        
        cur = TreeNode(rootVal)

        l = self.buildTree(preOrderLeft,inOrderLeft)
        r = self.buildTree(preOrderRight,inOrderRight)

        cur.left = l
        cur.right = r

        return cur




