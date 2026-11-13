# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            p = head

            if not p.next:
                return None

            while p.next and p.next.next:
                p = p.next
            
            p.next = None

            return head

        def reverseLinkedList(self, head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        # Reverse 1
        head_r = reverseLinkedList(self, head)
        # [2,1]
        
        p = head_r
        pos = 1

        while p and pos < n-1:
            p = p.next
            pos += 1

        # Have pos = n <=> Replace Here
        if p.next:
            temp = p.next.next
            p.next = temp

        head_2 = reverseLinkedList(self, head_r)

        return head_2
        
