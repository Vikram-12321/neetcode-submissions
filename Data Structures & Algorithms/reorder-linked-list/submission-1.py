# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # OG Order: [0, 1, 2, ..., n-3, n-2, n-1]
        # [0, n-1, 1, n-2, 2, n-3, ...]

        #1. Find middle (slow/fast pointers)
        #2. Slice first half and second half -> reverse second half
        #3. intertwine two lists

        #1. Find middle (slow/fast pointers)
        p_f, p_s = head, head

        while p_f and p_f.next:
            p_f = p_f.next.next
            p_s = p_s.next

        # Here, p_s is the pointer at the middle

        #2.  Slice first half and second half -> reverse second half
        
        temp = p_s.next
        head_2 = temp
        p_s.next = None #break the list

        #Reverse
        prev, curr = None, head_2

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #3 Interweave head_1 & head_2

        r1, r2 = head, prev

        while r2:
            n1, n2 = r1.next, r2.next 

            ## Input
            r1.next = r2
            r2.next = n1

            # Update Pointers 
            r1, r2 = n1, n2



