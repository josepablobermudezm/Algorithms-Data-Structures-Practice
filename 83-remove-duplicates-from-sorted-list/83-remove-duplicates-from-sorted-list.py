# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headAux = head
        
        if headAux:
            while headAux.next:
                if headAux.val == headAux.next.val:
                    headAux.next = headAux.next.next
                if headAux.next:
                    if headAux.val != headAux.next.val:
                        headAux = headAux.next
        return head
        