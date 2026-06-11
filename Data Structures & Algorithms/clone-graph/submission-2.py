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
        def travel(root):
            if root.val in h:
                return h[root.val]
            
            h[root.val] = Node(root.val)
            for n in root.neighbors:
                h[root.val].neighbors.append(travel(n))
            return h[root.val]
                
                    
        return travel(node)
            