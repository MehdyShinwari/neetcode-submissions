# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        slow = head
        while cur:
            slow = slow.next
            if cur == slow:
                return True
            cur = cur.next.next
        return False