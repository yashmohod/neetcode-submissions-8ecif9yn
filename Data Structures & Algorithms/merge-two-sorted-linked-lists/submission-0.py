# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(0,None)
        head = res
        while list1!= None or list2!= None:
            
            if list1 and list2:
                if list1.val < list2.val:
                    res.next = list1
                    res = res.next
                    tmp = list1.next
                    res.next = None
                    list1 = tmp
                else:
                    res.next = list2 
                    res = res.next
                    tmp = list2.next
                    res.next = None
                    list2 = tmp
            elif not list1:
                res.next = list2
                break
            else :
                res.next = list1
                break

        return head.next
