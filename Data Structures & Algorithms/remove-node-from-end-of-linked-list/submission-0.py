# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if n == 1:
            return head.next

        prev = None
        cur = head 
        while n >0:
            n-=1
            prev = cur
            cur = cur.next

        prev.next = cur.next

        return head