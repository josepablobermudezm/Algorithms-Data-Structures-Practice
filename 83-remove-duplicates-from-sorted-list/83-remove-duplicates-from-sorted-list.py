# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
#First approach

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
'''
  
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
