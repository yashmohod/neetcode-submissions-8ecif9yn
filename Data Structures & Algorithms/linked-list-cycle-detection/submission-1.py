# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        f = head
        s = head.next
        while s and f:
            if s.val == f.val:
                return True
            
            f = f.next.next
            s = s.next

        return False