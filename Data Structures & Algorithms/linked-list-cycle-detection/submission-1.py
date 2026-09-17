# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow_pointer = head
        fast_pointer = head

        while True:
            slow_pointer = slow_pointer.next
            
            if fast_pointer.next != None:
                fast_pointer = fast_pointer.next
                if fast_pointer.next != None:
                    fast_pointer = fast_pointer.next
                else:
                    return False
            else:
                return False

            if fast_pointer == slow_pointer:
                return True

        
            


            

            