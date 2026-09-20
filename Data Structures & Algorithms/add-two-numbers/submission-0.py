# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        takeover = 0
        while l1 and l2:
            comb = l1.val + l2.val + takeover
            takeover = 0
            if comb <10:
                cur.val = comb 
            else:
                cur.val = comb - 10
                takeover = 1
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                cur.next = ListNode()
                cur = cur.next

        while l1:
            cur.val = l1.val
            l1 = l1.next
            if l1:
                cur.next = ListNode()
                cur = cur.next
        while l2:
            cur.val = l2.val
            l2 = l2.next
            if l2:
                cur.next = ListNode()
                cur = cur.next
        if takeover:
            cur.next = ListNode()
            cur = cur.next
            cur.val = 1
        return dummy
