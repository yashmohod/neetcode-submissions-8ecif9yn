class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle with slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half in-place
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # prev is now the head of the reversed second half

        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:          # second half is shorter or equal
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



        
