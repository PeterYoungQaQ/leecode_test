# coding=utf-8
# @Time: 3/18/2019 2:01 PM


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                if cur.next.next is None:
                    cur.next = None
                else:
                    temp = cur.next.next
                    cur.next = temp
            else:
                cur = cur.next
        return head


