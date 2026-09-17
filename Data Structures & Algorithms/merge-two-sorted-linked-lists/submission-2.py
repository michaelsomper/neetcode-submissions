# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2

        current = None
        left = list1
        right = list2

        if list1.val < list2.val:
            current = list1
            left = list1.next
        else:
            current = list2
            right = list2.next

        first = current

        while left and right:
            if left.val < right.val:
                current.next = left
                current = current.next
                left = left.next
            else:
                current.next = right
                current = current.next
                right = right.next
        
        while left:
            current.next = left
            current = current.next
            left = left.next
        
        while right:
            current.next = right
            current = current.next
            right = right.next

        return first



        