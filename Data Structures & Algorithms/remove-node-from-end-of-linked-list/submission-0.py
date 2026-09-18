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
        cur = head
        print(i, n)
        for x in range(1, i-n):
            cur=cur.next
        if cur.next:
            cur.next = cur.next.next
        else:
            return None
        return head