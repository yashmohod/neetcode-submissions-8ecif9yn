# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head==None or head.next == None:
            return False
        f = head
        s = head.next
        while s and f:
            if s.val == f.val:
                return True
            
            f = f.next
            s = s.next.next

        return False