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


        original = head
        copy = Node(head.val)
        copy_head = copy
        lb = {copy.val:copy}
        while original.next:
            copy.next = Node(original.next.val)
            copy = copy.next
            lb[copy.val] = copy
            original = original.next
        
        original = head
        while original:
            lb[original.val].random = lb[original.random.val] if original.random else None
            original = original.next
        
        return copy_head