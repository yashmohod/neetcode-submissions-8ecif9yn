# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def kth(n:int,cur:Optional[ListNode])-> Optional[ListNode]:
            while cur and n >0:
                cur = cur.next
                n -=1
            return cur
        
        res = ListNode(0,head)
        prev = res

        while True:

            kNode = kth(k,prev)
            if not kNode:
                break
            
            rest = kNode.next
            
            pn = kNode.next
            start = prev.next
            
            while start != rest:
                tmp = start.next
                start.next = pn
                pn = start
                start = tmp
            
            tmp = prev.next
            prev.next = kNode
            prev = tmp

        return  res.next                
                
