# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        res = 0

        q = deque([(root,0)])

        while q:
            cur,height = q.popleft()
            res = max(height+1,res) if cur else res
            if cur and cur.left:
                q.append((cur.left,height+1)) 
            if cur and cur.right:
                q.append((cur.right,height+1))
        
        return res