# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head==None or head.next == None:
            return False
        f = head.next
        s = head.next.next
        while s and s.next:
            if s.val == f.val:
                return True
            
            f = f.next
            s = s.next.next 

        return False