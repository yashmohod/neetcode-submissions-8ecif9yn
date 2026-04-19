# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([(root,0)])

        while q:
            cur,idx = q.pop()
            if len(res) < idx+1:
                res.append([cur.val])
            else:
                res[idx].append(cur.val)
            
            if cur.left:
                q.append((cur.left,idx+1))
            if cur.right:
                q.append((cur.right,idx+1))
        for i in res:
            i.reverse()
        return res
