# coding=utf-8 
# @Time :2019/2/17 17:12

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode(-1)
        tail = pre

        q = head
        while q is not None:
            # 向后查找k个节点
            n = k
            p = q
            while p is not None and n > 0:
                p = p.next
                n -= 1

            # 如果在查找k个节点的过程中遇到None，则说明
            # 后面的节点不够k个节点则直接跳出即可
            if n > 0:
                tail.next = q
                break

            # 将这K个节点以头插法插入
            end = q
            while q != p:
                t = q.next
                q.next = tail.next
                tail.next = q
                q = t
            tail = end
        return pre.next
