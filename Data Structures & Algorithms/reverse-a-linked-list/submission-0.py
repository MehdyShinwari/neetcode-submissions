# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res1 = res
        tmp = []
        if not head:
            return head
        while head != None:
            tmp.append(head.val)
            head = head.next
        for i in range(len(tmp) -1, -1, -1):
            res.val = tmp[i]
            if i != 0:
                res.next = ListNode()
                res = res.next
        return res1