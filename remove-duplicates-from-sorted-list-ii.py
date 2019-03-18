# coding=utf-8
# @Time: 3/18/2019 1:54 PM


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        only_list = []
        only_dict = {}

        head2 = ListNode(0)
        p = head2
        while head:
            if head.val in only_dict:
                only_dict[head.val] += 1
            else:
                only_list.append(head.val)
                only_dict[head.val] = 1
            head = head.next
        for i in only_list:
            if only_dict[i] == 1:
                new = ListNode(i)
                p.next = new
                p = p.next
        return head2.next


