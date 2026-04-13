# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = ListNode()
        cur = res

        while any(lists):

            cur_min = None
            cur_idx = 0 
            for idx,i in enumerate(lists):
                if i:
                    if cur_min:
                        if i.val <= cur_min.val:
                            cur_min = i
                            cur_idx = idx
                    else:
                        cur_min = i
                        cur_idx = idx
            
            if cur == None:
                break
            
            cur.next = cur_min
            cur = cur.next
            lists[cur_idx] = cur_min.next
        
        return res.next

