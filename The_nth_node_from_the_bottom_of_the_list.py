# coding=utf-8 
# @Time :2019/2/3 11:35


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        # 创建虚拟头结点
        dummy = ListNode(-1)
        dummy.next = head

        # 创建两个指针，并将指针p2移动n步
        p1, p2 = dummy, dummy
        for i in range(n):
            p2 = p2.next

        while p2.next:
            p1, p2 = p1.next, p2.next

        p1.next = p1.next.next

        return dummy.next



