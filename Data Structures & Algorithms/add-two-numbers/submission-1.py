# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c = 0 
        res = ListNode(0)
        r = res
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            som = a+b+c

            res.val = som%10
            c = som//10

            if c or (l1 and l1.next) or (l2 and l2.next):
                res.next=ListNode(c)
                res = res.next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return r 
            
