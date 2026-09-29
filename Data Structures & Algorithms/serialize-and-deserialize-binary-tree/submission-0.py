# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return "_"
        r = ["_"]
        q = deque([(root,1)])

        while q:
            cur, idx = q.popleft()
            while len(r)<idx+1:
                r.append("_")
            r[idx] = str(cur.val)
            
            if cur.left:
                q.append((cur.left,2*idx)) 
            if cur.right:
                q.append((cur.right,2*idx+1))
        ss = ",".join(r)
        return ss
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        ss = data.split(",")
        print(ss)

        if len(ss) <= 1:
            return None
        
        res = [None]*len(ss)
        for i in range(len(ss)-1, 0,-1):
            if i >= len(ss):
                res[i] = TreeNode(ss[i])
            else:
                if ss[i] != "_":
                    res[i] = TreeNode(ss[i])
                    res[i].left = res[i*2] if i*2 < len(ss) else None
                    res[i].right = res[2*i +1] if i*2 +1 < len(ss) else None
            
            if i == 1:
                return res[i]
        return None

