# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head.next
        slow = head
        while cur and cur.next and cur.next.next:
            if cur == slow:
                return True
            slow = slow.next
            cur = cur.next.next
        return False