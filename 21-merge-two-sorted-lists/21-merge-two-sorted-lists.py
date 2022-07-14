# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2
        current, aux = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = current
        while current and aux:
            while current.next and current.next.val < aux.val:
                current = current.next
            current.next, aux = aux, current.next
            current = current.next
        return head