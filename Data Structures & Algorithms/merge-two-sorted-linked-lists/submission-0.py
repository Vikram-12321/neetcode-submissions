# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1, p2 = list1, list2

        if not list1:
            return list2
        if not list2:
            return list1

        # choose the head explicitly
        if p1.val <= p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next
        
        p = head # Set pointer to head

        while p1 and p2:

            if p1.val <= p2.val:
                p.next = p1 #set pointer.next to p1
                p1 = p1.next

            else: ## p2.val < p1.val
                p.next = p2
                p2 = p2.next

            p = p.next # move pointer forward

        p.next = p1 or p2 # attach last bit to remaining 

        return head


