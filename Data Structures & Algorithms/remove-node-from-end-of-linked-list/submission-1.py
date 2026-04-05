# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        cur = head
        while cur:
            i+=1
            cur=cur.next
        
        k = i-n
        if k==0:
            return head.next
            
        prev = None
        cur = head
        while k >0:
            k-=1
            prev = cur
            cur = cur.next
        
        prev.next = cur.next

        return head
        