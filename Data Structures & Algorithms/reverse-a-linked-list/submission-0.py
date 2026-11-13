# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head # Initialize curr to head [0,1,2,3]
        prev = None # Starts at []. 

        while curr:
            nxt = curr.next  # Store the next thing, say [1,2,3]
            # Store next, [2,3]
            curr.next = prev # Point 1 to 0 
            # Set [1] next to [0]
            prev = curr # Point prev to 1 (where 1 points to 0)
            # Set prev = [0] to  [1]
            
            curr = nxt # set curr = [0] to [1]


        return prev