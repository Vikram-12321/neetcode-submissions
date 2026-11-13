# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        p_f, p_s = head, head #fast pointer, slower pointer

        while p_f and p_f.next:
            if p_f.next.next == p_s:
                return True
            else:
                p_f = p_f.next.next
                p_s = p_s.next


        return False

