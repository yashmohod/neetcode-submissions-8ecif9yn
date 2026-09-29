"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        h = {}
        visited =  set()
        def travel(root):
            if root.val in visited:
                return
            visited.add(root.val)
            for n in root.neighbors:
                    if n.val not in h:
                        h[n.val] = Node(n.val)
                        h[root.val].neighbors.append(h[n.val])
                        h[n.val].neighbors.append(h[root.val])
                        travel(n)
                    
        
        h[node.val] = Node(node.val)
        travel(node)
        return h[node.val]
            