# coding=utf-8
# @Time: 3/7/2019 1:32 PM


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        ListLen = 0
        p = head
        # 数有几个节点
        while p:
            ListLen += 1
            p = p.next

        k = k % ListLen
        if k == 0:
            return head

        p = head
        while k > 0:
            k -= 1
            p = p.next
        slow = head
        fast = p

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head
