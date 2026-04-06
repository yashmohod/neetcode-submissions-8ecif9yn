"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return None
        original = head
        copy = Node(head.val)
        copy_head = copy
        lb = {head:copy}
        while original.next:
            copy.next = Node(original.next.val)
            copy = copy.next
            lb[original.next] = copy
            original = original.next
        
        original = head
        while original:
            lb[original].random = lb[original.random] if original.random else None
            original = original.next
        
        return copy_head