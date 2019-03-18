# coding=utf-8
# @Time: 3/18/2019 3:49 PM


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def partition(head: ListNode, x: int) -> ListNode:
        head1 = ListNode(0)
        head2 = ListNode(0)
        phead1 = head1
        phead2 = head2
        tmp = head
        while tmp:
            if tmp.val < x:
                phead1.next = tmp
                tmp = tmp.next
                phead1 = phead1.next
                phead1.next = None
            else:
                phead2.next = tmp
                tmp = tmp.next
                phead2 = phead2.next
                phead2.next = None
        phead1.next = head2.next
        head = head1.next
        return head



