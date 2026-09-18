# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        cur = head
        while cur.next:
            cur = cur.next
            i += 1
        if n == i:
            return head.next
        cur = head

        for _ in range(i-n-1):
            cur=cur.next
        cur.next = cur.next.next
        return head