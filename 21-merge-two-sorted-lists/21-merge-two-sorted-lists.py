# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2
        first, second = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = first
        while first and second:
            while first.next and first.next.val < second.val :
                first = first.next
            first.next, second = second, first.next
            first = first.next
        return head
                
        
            
            
# first   1 - 1 - 2 - 3 - 4
# second  4
# current 

# 
            
                